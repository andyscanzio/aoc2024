from itertools import pairwise
from pathlib import Path
from re import compile

folder = Path(__file__).parent
test = folder / "test.txt"
input = folder / "input.txt"

with open(input, "r") as file:
    data = file.read()

REGISTER_PATTERN = compile(r"Register ([A-Z]): (\d+)")
PROGRAM_PATTERN = compile(r"Program: ((?:\d,?)+)")


class Computer:
    def __init__(self, data, debug=False):
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

            self.opcodes[opcode](operand)
        print(",".join(self.output))


Computer(data, True).run()
