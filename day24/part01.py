from pathlib import Path
from operator import and_, or_, xor
from collections import defaultdict, Counter, deque

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
wires = list(inputs.keys()) + list(gates.keys())
z_wires = sorted((wire for wire in wires if wire.startswith("z")), reverse=True)

sorted_wires = []
in_degree = Counter()
for wire in wires:
    for wire_to in edges[wire]:
        in_degree[wire_to] += 1
stack = deque([wire for wire in wires if in_degree[wire] == 0])
while stack:
    wire = stack.popleft()
    sorted_wires += [wire]
    for wire_to in edges[wire]:
        in_degree[wire_to] -= 1
        if in_degree[wire_to] == 0:
            stack.append(wire_to)
assert len(sorted_wires) == len(wires)

outputs = {}
for wire in sorted_wires:
    if wire in inputs:
        outputs[wire] = inputs[wire]
    else:
        wire1, op, wire2 = gates[wire]
        outputs[wire] = oper[op](outputs[wire1], outputs[wire2])
binary_result = "".join(map(str, [outputs[wire] for wire in z_wires]))
print(int(binary_result, 2))
