from typing import Any, Tuple


def to_bin(number: int) -> str:
    return bin(number)[2:]


def to_int(bin_str: str) -> int:
    return int(bin_str, 2)


def read_all(file_name: str) -> tuple[dict[str, str], list[Any] | list[str]]:
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
    return registers_bin, program_bin


def get_combo_operand_bin(input_operand_bin: str) -> str:
    if input_operand_bin == '100':
        return this_register_bin['A']
    elif input_operand_bin == '101':
        return this_register_bin['B']
    elif input_operand_bin == '110':
        return this_register_bin['C']
    else:
        as_int = to_int(input_operand_bin)
        if as_int > 3 or as_int < 0:
            print(f'input_operand_bin {input_operand_bin} which is {as_int}')
        return input_operand_bin


def division_bin(dividend, divisor) -> Tuple[str, str]:
    # Initialize quotient and remainder as strings
    quotient = ''
    remainder = ''

    # Precompute divisor length and integer value
    divisor_len = len(divisor)
    divisor_int = int(divisor, 2)

    for bit in dividend:
        # Shift left by appending current bit to remainder
        remainder += bit

        # Remove leading zeros from remainder
        remainder = remainder.lstrip('0')

        # Compare remainder with divisor
        if len(remainder) >= divisor_len and int(remainder, 2) >= divisor_int:
            # Subtract divisor from remainder
            temp_remainder = int(remainder, 2) - divisor_int
            remainder = bin(temp_remainder)[2:]
            quotient += '1'
        else:
            quotient += '0'

    quotient_output = quotient.lstrip('0')
    if len(quotient_output) == 0:
        quotient_output = '0'

    return quotient_output, remainder


def modulo_bin(binary_string: str) -> str:
    # Initialize remainder as a binary string
    remainder = '0'

    # Iterate over each bit in the binary string
    for bit in binary_string:
        # Update remainder for each bit
        # Convert remainder to integer, perform modulo, and convert back to binary
        remainder = bin((int(remainder, 2) * 2 + int(bit)) % 8)[2:]

    # Ensure the remainder is represented as a binary string
    return remainder  # Pad with leading zeros to


def power_bin(bin_num) -> str:
    # Initialize the decimal value of bin_num
    decimal_value = 0

    # Calculate the decimal value of bin_num without direct conversion
    for bit in bin_num:
        decimal_value = decimal_value * 2 + int(bit)

    # Compute 2^decimal_value in binary by shifting '1' left
    result = '1' + '0' * decimal_value

    return result


def xor_bin(bin1, bin2) -> str:
    # Pad the shorter string with leading zeros
    max_len = max(len(bin1), len(bin2))
    bin1 = bin1.zfill(max_len)
    bin2 = bin2.zfill(max_len)

    # Perform XOR operation bit by bit
    result = []
    for b1, b2 in zip(bin1, bin2):
        # XOR operation: 1 if bits are different, 0 if they are the same
        result.append('1' if b1 != b2 else '0')

    # Join the result list to form the final binary string
    return ''.join(result)


def is_binary_zero(binary_string) -> bool:
    # Strip all zeros and check if the result is empty
    return binary_string.strip('0') == ''


# his_register, this_program_input,

# READ DATA
# this_register_bin, this_program_input_bin = read_all('data/11.txt')
this_register_bin, this_program_input_bin = read_all('data/task1.txt')
# print(this_register)
# print(this_register_bin)
# print(this_program_input)
# print(this_program_input_bin)

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

output_bin = []

instruction_pointer = 0

while True:
    if instruction_pointer < len(this_program_input_bin):

        instruction_number = to_int(this_program_input_bin[instruction_pointer])
        operand_as_bit = this_program_input_bin[instruction_pointer + 1]

        # adv
        if instruction_number == 0:
            this_register_bin['A'] = \
                division_bin(this_register_bin['A'], power_bin(get_combo_operand_bin(operand_as_bit)))[0]
            instruction_pointer += 2

        # bxl
        elif instruction_number == 1:
            this_register_bin['B'] = xor_bin(this_register_bin['B'], operand_as_bit)
            instruction_pointer += 2

        # bst
        elif instruction_number == 2:
            this_register_bin['B'] = modulo_bin(get_combo_operand_bin(operand_as_bit))
            instruction_pointer += 2

        # jnz
        elif instruction_number == 3:
            if is_binary_zero(this_register_bin['A']):
                instruction_pointer += 2
            else:
                instruction_pointer = to_int(operand_as_bit)

        # bxc
        elif instruction_number == 4:
            this_register_bin['B'] = xor_bin(this_register_bin['B'], this_register_bin['C'])
            instruction_pointer += 2

        # out
        elif instruction_number == 5:
            output_bin.append(modulo_bin(get_combo_operand_bin(operand_as_bit)))
            instruction_pointer += 2

        # bdv
        elif instruction_number == 6:
            print('66666666666666')
            this_register_bin['B'] = \
            division_bin(this_register_bin['A'], power_bin(get_combo_operand_bin(operand_as_bit)))[0]

            instruction_pointer += 2

        # cdv
        elif instruction_number == 7:
            print('777777777777777777')
            print(f'       this_register_bin[A] {this_register_bin['A']}')
            print(f'       operand_as_bit {operand_as_bit}')

            this_register_bin['C'] = \
            division_bin(this_register_bin['A'], power_bin(get_combo_operand_bin(operand_as_bit)))[0]

            instruction_pointer += 2
        else:
            print(f'ARALRMO {instruction_number}')
    else:
        break

# print(output_bin)
output_nomal = [to_int(x) for x in output_bin]
print(','.join(map(str, output_nomal)))

print(this_register_bin)

print('hurray!')

# 0,0,0,0,0,0,0,0,0
# 1,7,7,0,5,7,3,2,7
# 7,7,4,6,3,2,4,2,7

# alt
# 3,3,3,7,7,7,4,3,6

# normal
# 6,0,3,6,6,5,7,0,0


# n1 = '1100'
# n2 = '1010'
#
# print(to_int(n1))
# print(to_int(n2))
# print(to_int(n1) ^ to_int(n2))
#
# print(n1)
# print(n2)
# print(xor_bin(n1, n2))
# print(to_int(xor_bin(n1, n2)))
