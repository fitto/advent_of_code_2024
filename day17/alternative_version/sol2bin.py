import copy
from typing import Any, Tuple


# from day17.helpers.h2 import ALL_A_ENDINGS


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

    if len(binary_string) == 0:
        binary_string = '0'

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

    output = ''.join(result)
    if len(output) == 0:
        return '0'

    # Join the result list to form the final binary string
    return output


def is_binary_zero(binary_string) -> bool:
    return binary_string.strip('0') == ''


# READ DATA
# original_this_register_bin, original_this_program_input_bin = read_all('data/22.txt')
original_this_register_bin, original_this_program_input_bin = read_all('../data/task1.txt')

DEBUG = False

int_found = None
# this_i_in_bit = (3 * 16 - 1) * '0'
# this_i_in_bit = '1' + this_i_in_bit
# i_as_bin_prefix = '11100000100000000010101000100111'
# this_i_in_bit = '1010100010101001010011011101'
# this_i_in_bit= to_bin(64854237)
prefix = to_bin(0)
# this_i_in_bit += '101001100'


# suffix = '101001100'

options = {}

iterations = 0

this_register_bin = {x: y for x, y in original_this_register_bin.items()}
this_program_input_bin = copy.deepcopy(original_this_program_input_bin)

matchin_max_no = 0

suffix = ''
this_i = prefix+ suffix

while int_found is None and iterations < 1024:
    # this_i_in_bit = i_as_bin_prefix
    # + i_as_bin_suffix)
    num = prefix + suffix
    this_register_bin['A'] = prefix + suffix
    # print(f'checking {this_is_in_bit}')
    # if len(this_register_bin) > 48:
    #     print('PROBLEM')
    #     print('PROBLEM')
    #     print('PROBLEM')

    instruction_pointer = 0
    output_bin = []

    while True:
        if instruction_pointer < len(this_program_input_bin):
            instruction_number = to_int(this_program_input_bin[instruction_pointer])
            operand_as_bit = this_program_input_bin[instruction_pointer + 1]

            # adv
            if instruction_number == 0:
                if DEBUG:
                    print(
                        f'doing 0 output saved to A is {division_bin(this_register_bin['A'], power_bin(get_combo_operand_bin(operand_as_bit)))[0]}')
                    print(operand_as_bit)
                    print(get_combo_operand_bin(operand_as_bit))
                    print(power_bin(get_combo_operand_bin(operand_as_bit)))

                this_register_bin['A'] = \
                    division_bin(this_register_bin['A'], power_bin(get_combo_operand_bin(operand_as_bit)))[0]
                instruction_pointer += 2

            # bxl
            elif instruction_number == 1:
                if DEBUG:
                    print(f'doing 1 output set to B is {xor_bin(this_register_bin['B'], operand_as_bit)}')
                this_register_bin['B'] = xor_bin(this_register_bin['B'], operand_as_bit)
                instruction_pointer += 2

            # bst
            elif instruction_number == 2:
                if DEBUG:
                    print(f'doing 2 output set to B is {modulo_bin(get_combo_operand_bin(operand_as_bit))}')
                this_register_bin['B'] = modulo_bin(get_combo_operand_bin(operand_as_bit))
                instruction_pointer += 2

            # jnz
            elif instruction_number == 3:
                if DEBUG:
                    print(f'doing 3 output A is {this_register_bin['A']}')
                if is_binary_zero(this_register_bin['A']):
                    if DEBUG:
                        print(f'so adding 2')
                    instruction_pointer += 2
                else:
                    instruction_pointer = to_int(operand_as_bit)
                    if DEBUG:
                        print(f'so instruction_pointer={to_int(operand_as_bit)}')

            # bxc
            elif instruction_number == 4:
                if DEBUG:
                    print(f'doing 4 output set to B is {xor_bin(this_register_bin['B'], this_register_bin['C'])}')
                this_register_bin['B'] = xor_bin(this_register_bin['B'], this_register_bin['C'])
                instruction_pointer += 2

            # out
            elif instruction_number == 5:
                if DEBUG:
                    print(f'doing 5 output is {modulo_bin(get_combo_operand_bin(operand_as_bit))}')
                output_bin.append(modulo_bin(get_combo_operand_bin(operand_as_bit)))

                # if to_int(output_bin[0]) != 2:
                #     # print(this_i_in_bit)
                #     print('STH Went wrong')
                #     if DEBUG:
                #         print('LEAVING')
                #     # break

                # if len(output_bin) > len(original_this_program_input_bin):
                #     iterations += 1
                #
                #     instruction_pointer += 10000
                #     print('TOO LONG STRING')
                #     if DEBUG:
                #         print('LEAVING')
                #     # break
                #
                # n = 0
                # while n < len(original_this_program_input_bin) and n < len(output_bin):
                #     if output_bin[n] == original_this_program_input_bin[n]:
                #         matchin_max_no = max(n, matchin_max_no)
                #     else:
                #         instruction_pointer += 10000
                #     n += 1

                # n +=1
                # for n in range(len(output_bin)):
                #     if output_bin[n] != original_this_program_input_bin[n]:
                #         # print('pruning')
                #         iterations += 1
                #         instruction_pointer += 10000
                #         if DEBUG:
                #             print('LEAVING')

                # break
                # print(output_bin)

                instruction_pointer += 2

            # bdv
            elif instruction_number == 6:
                if DEBUG:
                    print(f'doing 6')
                this_register_bin['B'] = \
                    division_bin(this_register_bin['A'], power_bin(get_combo_operand_bin(operand_as_bit)))[0]

                instruction_pointer += 2

            # cdv
            elif instruction_number == 7:
                if DEBUG:
                    print(
                        f'doing 7 output set to C is {division_bin(this_register_bin['A'], power_bin(get_combo_operand_bin(operand_as_bit)))[0]}')
                this_register_bin['C'] = \
                    division_bin(this_register_bin['A'], power_bin(get_combo_operand_bin(operand_as_bit)))[0]

                instruction_pointer += 2
            else:
                print(f'ARALRMO {instruction_number}')
        else:
            options[num] = output_bin
            break

    if output_bin == original_this_program_input_bin:
        int_found = to_int(num)
        print('-------------------------------')
        print('found')
        print('-------------------------------')
        break

    prefix = to_bin(to_int(prefix) + 1)

    iterations += 1
    if iterations % 100000 == 0:
        print(
            f'i = {iterations} and this_i_in_bit is {prefix} which is {[to_int(x) for x in output_bin]} and {matchin_max_no} max matching ')

# options = {k: v for k,v in options.items() if len(v) > 7}
# options = {k: v for k,v  in options.items() if
#            v[0] == '10'
#            and v[1] == '100'
#            # and to_int(v[2]) == 1
#            # and to_int(v[3]) == 1
#            # and to_int(v[4]) == 7
#            # and to_int(v[5]) == 5
#            # and to_int(v[6]) == 1
#            # and to_int(v[7]) == 5
#            }
sorted_dict = dict(sorted(options.items(), key=lambda item: item[1]))



print(int_found)
print('hurray!')
print(int_found)
