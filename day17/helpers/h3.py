import copy
from typing import Tuple

from day17.helpers.h2 import ALL_A_ENDINGS


def to_bin(number: int) -> str:
    return bin(number)[2:]


def to_int(bin_str: str) -> int:
    return int(bin_str, 2)


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


LNGTH_P = 65

SOL = [2, 4, 1, 1, 7, 5, 1, 5, 4, 0, 5, 5, 0, 3, 3, 0]
SOL_SUFFIXES_DATA = {0: copy.deepcopy(ALL_A_ENDINGS)}


def check_a(a_number: str,
            expected: str
            ) -> bool:
    b_number = modulo_bin(a_number)
    b_number = xor_bin(b_number, '1')
    c_number = division_bin(a_number, power_bin(b_number))[0]
    b_number = xor_bin(b_number, '101')
    b_number = xor_bin(b_number, c_number)

    outcome = modulo_bin(b_number)
    return outcome == expected


def find_digits(digit_number: int):
    expected_outcome = to_bin(SOL[digit_number])

    suffix_data_for_int = SOL_SUFFIXES_DATA[digit_number]
    this_len = len(suffix_data_for_int[0])

    all_possible_prefixes = [format(i, '03b') for i in range(2 ** (LNGTH_P - this_len))]
    all_possible_prefixes = [x.zfill(LNGTH_P) for x in all_possible_prefixes]
    all_possible_prefixes = list(set(all_possible_prefixes))

    all_valid_a_s = set()

    for prefix in all_possible_prefixes:
        for suffix in suffix_data_for_int:
            a_number = prefix + suffix
            a_number = division_bin(a_number, '1000')[0]
            if check_a(a_number, expected_outcome):
                max_lngth = 65
                a_length = len(a_number)
                no = min(max_lngth, a_length)

                all_valid_a_s.add(a_number[-no:])

    return all_valid_a_s


for i in range(len(SOL)):
    x = find_digits(i)
    SOL_SUFFIXES_DATA[i + 1] = copy.deepcopy(x)

    print(f'done {i} and found {len(SOL_SUFFIXES_DATA[i + 1])} suffixes')
    # print(SOL_SUFFIXES_DATA[i])

print(SOL_SUFFIXES_DATA[len(SOL_SUFFIXES_DATA) - 1])
