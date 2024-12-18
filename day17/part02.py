from itertools import pairwise
from pathlib import Path
from re import compile
from copy import deepcopy

folder = Path(__file__).parent
test = folder / "test.txt"
input = folder / "input.txt"

with open(input, "r") as file:
    data = file.read()

REGISTER_PATTERN = compile(r"Register ([A-Z]): (\d+)")
PROGRAM_PATTERN = compile(r"Program: ((?:\d,?)+)")


class Computer:
    def __init__(self, data, reg_a, debug=False):
        self.debug = debug
        self.register = {}
        self.opcodes = {
            "0": self.adv,
            "1": self.bxl,
            "2": self.bst,
            "3": self.jnz,
            "4": self.bxc,
            "5": self.out,
            "6": self.bdv,
            "7": self.cdv,
        }
        self.output = []
        self.pc = 0

        for reg, val in REGISTER_PATTERN.findall(data):
            self.register[reg] = int(val)
        [t] = PROGRAM_PATTERN.findall(data)
        self.program = t.split(",")
        self.program_string = t
        self.register["A"] = reg_a

    def combo_operand(self, operand):
        if operand in (0, 1, 2, 3):
            return operand
        elif operand == 4:
            return self.register["A"]
        elif operand == 5:
            return self.register["B"]
        elif operand == 6:
            return self.register["C"]
        else:
            raise ValueError

    def adv(self, operand):
        if self.debug:
            print("adv", operand)
        self.register["A"] = self.register["A"] // (2 ** self.combo_operand(operand))
        self.pc += 2

    def bxl(self, operand):
        if self.debug:
            print("bxl", operand)
        self.register["B"] = self.register["B"] ^ operand
        self.pc += 2

    def bst(self, operand):
        if self.debug:
            print("bst", operand)
        self.register["B"] = self.combo_operand(operand) % 8
        self.pc += 2

    def jnz(self, operand):
        if self.debug:
            print("jnz", operand)
        if self.register["A"] == 0:
            self.pc += 2
        else:
            self.pc = operand

    def bxc(self, operand):
        if self.debug:
            print("bxc", operand)
        self.register["B"] = self.register["B"] ^ self.register["C"]
        self.pc += 2

    def out(self, operand):
        if self.debug:
            print("out", operand)
        self.output.append(str(self.combo_operand(operand) % 8))
        self.pc += 2

    def bdv(self, operand):
        if self.debug:
            print("bdv", operand)
        self.register["B"] = self.register["A"] // (2 ** self.combo_operand(operand))
        self.pc += 2

    def cdv(self, operand):
        if self.debug:
            print("cdv", operand)
        self.register["C"] = self.register["A"] // (2 ** self.combo_operand(operand))
        self.pc += 2

    def run(self):
        while self.pc < len(self.program):
            if self.debug:
                print("pc", self.pc)
            opcode = self.program[self.pc]
            operand = int(self.program[self.pc + 1])
            if opcode == "5":
                return self.combo_operand(operand) % 8, self.register["A"]
            self.opcodes[opcode](operand)

        return True, ",".join(self.output)


expected = tuple(map(int, PROGRAM_PATTERN.findall(data)[0].split(",")))

place = len(expected) - 1
curr_reg_a = [0]

while place >= 0:
    next_reg_a = []
    expected_output = expected[place]
    for reg_a in curr_reg_a:
        new_reg_a = reg_a * 8
        for y in range(8):
            tested_reg_a = new_reg_a + y
            NewOutput, PassedA = Computer(data, tested_reg_a).run()
            if NewOutput == expected_output:
                next_reg_a.append(tested_reg_a)

    place -= 1
    curr_reg_a = deepcopy(next_reg_a)
print(min(curr_reg_a))
