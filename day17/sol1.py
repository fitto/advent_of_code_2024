from math import floor
from typing import Any


def to_bin(number: int) -> str:
    return bin(number)[2:]


def to_int(bin_str: str) -> int:
    return int(bin_str, 2)


def read_all(file_name: str) -> tuple[dict[str, int], list[Any] | list[int]]:
    registers = {}
    registers_bin = {}
    program = []
    program_bin = []

    with open(file_name, "r") as file:
        lines = file.readlines()

        for line in lines:
            if line.startswith('Register '):
                reg = line.rstrip()[len('Register '):].strip()
                registers[reg[0]] = int(reg.split(' ')[1])
                registers_bin[reg[0]] = to_bin(registers[reg[0]])

            if line.startswith('Program: '):
                p = line.rstrip()[len('Program: '):].strip()
                program = p.split(',')
                program = [int(x) for x in program]
                program_bin = [to_bin(x) for x in program]

    # registers, program,
    return registers, program


def get_combo_operand(input_operand_bin: int) -> int:
    if input_operand_bin == 4:
        return this_register['A']
    elif input_operand_bin == 5:
        return this_register['B']
    elif input_operand_bin == 6:
        return this_register['C']
    else:
        return input_operand_bin


# this_register, this_program_input = read_all('data/11.txt')
this_register, this_program_input = read_all('data/task1.txt')

# # # TEST1
# this_register_bin = {'C': '1001'}
# this_program_input_bin = ['10', '110']

# # # TEST2
# this_register_bin = {'A': to_bin(10)}
# this_test_input = [5, 0, 5, 1, 5, 4]
# this_program_input_bin = [to_bin(x) for x in this_test_input]

# # # TEST3
# this_register_bin = {'A': to_bin(2024)}
# this_test_input = [0, 1, 5, 4, 3, 0]
# this_program_input_bin = [to_bin(x) for x in this_test_input]

# # # TEST4
# this_register_bin = {'B': to_bin(29)}
# this_test_input = [1, 7]
# this_program_input_bin = [to_bin(x) for x in this_test_input]

# # # TEST5
# this_register_bin = {'B': to_bin(2024), 'C': to_bin(43690)}
# this_test_input = [4, 0]
# this_program_input_bin = [to_bin(x) for x in this_test_input]

output = []

instruction_pointer = 0

while True:
    if instruction_pointer < len(this_program_input):

        instruction_number = this_program_input[instruction_pointer]
        operand = this_program_input[instruction_pointer + 1]

        # adv
        if instruction_number == 0:
            this_register['A'] = floor(this_register['A'] / (2 ** get_combo_operand(operand)))
            instruction_pointer += 2

        # bxl
        elif instruction_number == 1:
            this_register['B'] = this_register['B'] ^ operand
            instruction_pointer += 2

        # bst
        elif instruction_number == 2:
            this_register['B'] = operand % 8
            instruction_pointer += 2

        # jnz
        elif instruction_number == 3:
            if this_register['A'] == 0:
                instruction_pointer += 2
            else:
                instruction_pointer = operand

        # bxc
        elif instruction_number == 4:
            this_register['B'] = this_register['B'] ^ this_register['C']
            instruction_pointer += 2

        # out
        elif instruction_number == 5:
            output.append(get_combo_operand(operand) % 8)
            instruction_pointer += 2

        # bdv
        elif instruction_number == 6:
            this_register['B'] = floor(this_register['A'] / (2 ** get_combo_operand(operand)))
            instruction_pointer += 2

        # cdv
        elif instruction_number == 7:
            this_register['C'] = floor(this_register['A'] / (2 ** get_combo_operand(operand)))
            instruction_pointer += 2
        else:
            print(f'ARALRMO {instruction_number}')
    else:
        break

# print(output_bin)
print(','.join(map(str, output)))

print(this_register)

print('hurray!')

# 0,0,0,0,0,0,0,0,0
# 1,7,7,0,5,7,3,2,7
# 7,7,4,6,3,2,4,2,7

# alt
# 3,3,3,7,7,7,4,3,6

# normal
# 6,0,3,6,6,5,7,0,0
