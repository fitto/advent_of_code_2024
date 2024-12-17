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


def modulo_bin(binary_string: str) -> str:
    # Initialize remainder as a binary string
    remainder = '0'

    # Iterate over each bit in the binary string
    for bit in binary_string:
        # Update remainder for each bit
        # Convert remainder to integer, perform modulo, and convert back to binary
        remainder = bin((int(remainder, 2) * 2 + int(bit)) % 8)[2:]

    # Ensure the remainder is represented as a binary string
    return remainder


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


# this_register_bin, this_program_input_bin = read_all('data/11.txt')
this_register_bin, this_program_input_bin = read_all('data/task1.txt')

output_bin = []
while this_register_bin['A'] != '0':
    future_a, future_a_reminder = division_bin(this_register_bin['A'], '1000')

    # 2, 4
    this_register_bin['B'] = future_a_reminder
    # 1, 1
    this_register_bin['B'] = xor_bin(this_register_bin['A'], '1')
    # 7, 5
    this_register_bin['C'] = division_bin(future_a, '101')[0]
    # 1, 5
    this_register_bin['B'] = xor_bin(this_register_bin['A'], '101')
    # 4, 0
    this_register_bin['B'] = xor_bin(this_register_bin['B'], this_register_bin['C'])
    # 5, 5
    output_bin.append(modulo_bin(this_register_bin['B']))

    # 0, 3
    this_register_bin['A'] = future_a

output_nomal = [to_int(x) for x in output_bin]
print(','.join(map(str, output_nomal)))

print('hurray!')

# 3,3,3,7,7,7,4,3,6