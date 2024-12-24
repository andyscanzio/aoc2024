from pathlib import Path
from operator import and_, or_, xor
from collections import defaultdict

folder = Path(__file__).parent
test = folder / "test.txt"
input = folder / "input.txt"

with open(input, "r") as file:
    data = file.read()

oper = {"XOR": xor, "AND": and_, "OR": or_}

init_reg, temp_sequence = data.split("\n\n")

inputs = {key: int(val) for key, val in (i.split(": ") for i in init_reg.splitlines())}
gates = {}
edges = defaultdict(list)  # edges/order
for line in temp_sequence.splitlines():
    left, output_wire = line.split(" -> ")
    wire1, op, wire2 = left.split()
    gates[output_wire] = (wire1, op, wire2)
    edges[wire1] += [output_wire]
    edges[wire2] += [output_wire]


gate_and = [None] * 45
gate_xor = [None] * 45
gate_z = [None] * 45
gate_tmp = [None] * 45
gate_carry = [None] * 45

swaps = []


def find_rule(wire1, operation, wire2):
    for output_wire, (w1, op, w2) in gates.items():
        if (wire1, operation, wire2) in [(w1, op, w2), (w2, op, w1)]:
            return output_wire
    return None


def swap(wire1, wire2):
    global swaps
    gates[wire1], gates[wire2] = gates[wire2], gates[wire1]
    swaps += [wire1, wire2]
    # print(f"*** Swapping {wire1} and {wire2}; swaps={swaps}.")


# bit 0 (this bit is ok in MY input)
i = 0
x = f"x{str(i).zfill(2)}"
y = f"y{str(i).zfill(2)}"
gate_and[i] = find_rule(x, "AND", y)
gate_xor[i] = find_rule(x, "XOR", y)
gate_z[i] = gate_xor[i]
gate_carry[i] = gate_and[i]
# print(f"bit={i}:  and={gate_and[i]}  xor={gate_xor[i]}  z={gate_z[i]}  tmp={gate_tmp[i]}  carry={gate_carry[i]}")

# The logic below works for MY input.
# For other inputs, additional correction/swap logic might have to be added.
for i in range(1, 45):
    x = f"x{str(i).zfill(2)}"
    y = f"y{str(i).zfill(2)}"
    z = f"z{str(i).zfill(2)}"
    check = True
    while check:
        check = False

        gate_and[i] = find_rule(x, "AND", y)

        gate_xor[i] = find_rule(x, "XOR", y)
        # The xor gate should appear as an input for the z gate.
        w1, op, w2 = gates[z]
        if w1 == gate_carry[i - 1] and w2 != gate_xor[i]:
            swap(w2, gate_xor[i])
            check = True
            continue
        if w2 == gate_carry[i - 1] and w1 != gate_xor[i]:
            swap(w1, gate_xor[i])
            check = True
            continue

        gate_z[i] = find_rule(gate_xor[i], "XOR", gate_carry[i - 1])
        # The output of the z gate should be z.
        if gate_z[i] != z:
            swap(gate_z[i], z)
            check = True
            continue

        gate_tmp[i] = find_rule(gate_xor[i], "AND", gate_carry[i - 1])

        gate_carry[i] = find_rule(gate_tmp[i], "OR", gate_and[i])

        # print(f"bit={i}:  and={gate_and[i]}  xor={gate_xor[i]}  z={gate_z[i]}  tmp={gate_tmp[i]}  carry={gate_carry[i]}")

assert len(swaps) == 8

print(",".join(sorted(swaps)))
