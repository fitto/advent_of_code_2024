import operator
from typing import Dict, List, Tuple, Optional


# def read_all(file_name: str) -> Tuple[Dict[str, int], List[int]]:
#     registers = {}
#     program = []
#
#     with open(file_name, "r") as file:
#         lines = file.readlines()
#
#         for line in lines:
#             if line.startswith('Register '):
#                 reg = line.rstrip()[len('Register '):].strip()
#                 registers[reg[0]] = int(reg.split(' ')[1])
#
#             if line.startswith('Program: '):
#                 p = line.rstrip()[len('Program: '):].strip()
#                 program = p.split(',')
#                 program = [int(x) for x in program]
#
#     return registers, program
#
#
# reg, pr = read_all('data/11.txt')

# tc1
reg, pr = {'C': 9, 'B': 0, 'A': 0}, [2, 6]

REGISTER = reg


def get_combo_operand(input_operand: int) -> Optional[int]:
    if -1 < input_operand < 4:
        return input_operand
    elif input_operand == 4:
        return REGISTER['A']
    elif input_operand == 5:
        return REGISTER['B']
    elif input_operand == 6:
        return REGISTER['C']
    else:
        print('ALARMOOOO')
        return None


def adv(operand: int):
    result = int(REGISTER['A'] / 2 ** get_combo_operand(operand))
    REGISTER['A'] = result


def bxl(operand: int):
    result = operator.xor(REGISTER['B'], operand)
    REGISTER['B'] = result


def bst(operand: int):
    result = operand & (8 - 1)
    # & 0xFF)
    REGISTER['B'] = result


def jnz(operand: int) -> int:
    if REGISTER['A'] != 0:
        return 0
    else:
        return operand


def bxc(operand: int):
    result = REGISTER['B'] ^ REGISTER['C']
    REGISTER['C'] = result


def out(operand: int):
    result = get_combo_operand(operand) & ((1 << 3) - 1)
    # & 0xFF)
    return result


def bdv(operand: int):
    result = int(REGISTER['A'] / 2 ** get_combo_operand(operand))
    REGISTER['B'] = result


def cdv(operand: int):
    result = int(REGISTER['A'] / 2 ** get_combo_operand(operand))
    REGISTER['C'] = result


INSTRUCTIONS_DICT = {
    0: adv,
    1: bxl,
    2: bst,
    3: jnz,  # jumpz
    4: bxc,
    5: out,
    6: bdv,
    7: cdv
}


# inst OpCode
# operand


def run_program(program: List[int],

                ):
    instruction_pointer = 0
    output = []
    while True:
        if instruction_pointer < len(program):
            # read the instruction
            instruction_int = program[instruction_pointer]

            print(f'instruction_int {instruction_int}')

            if instruction_int == 5:
                x = INSTRUCTIONS_DICT[instruction_int](program[instruction_pointer] + 1)
                output.append(x)
                instruction_pointer += 2

            else:
                x = INSTRUCTIONS_DICT[instruction_int](program[instruction_pointer] + 1)

                if x is None or x != 0:
                    instruction_pointer += 2
                else:
                    instruction_pointer = x

        else:
            return output


print(reg)
print(pr)

a = run_program(pr)
print(a)
