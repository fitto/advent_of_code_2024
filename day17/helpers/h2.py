from typing import Tuple


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


LNGTH_P = 18
STR_LNGTH = 8

all_options = []

all_possible_a_endings = [format(i, '03b') for i in range(2 ** LNGTH_P)]
all_possible_a_endings = [x.zfill(LNGTH_P) for x in all_possible_a_endings]
all_possible_a_endings = list(set(all_possible_a_endings))
print(len(all_possible_a_endings))

# i = 1
while len(all_possible_a_endings) > 0:
    a = all_possible_a_endings.pop()
    # a = '100000000000000000000000000001110111111111100010'

    b1 = modulo_bin(a)
    b2 = xor_bin(b1, '1')
    div = power_bin(b2)
    c = division_bin(a, power_bin(b2))[0]
    b4 = xor_bin(b2, '101')
    b5 = xor_bin(b4, c)

    last_3 = modulo_bin(b5)
    if to_int(last_3) == 2:
        this_power = '1000'
        a2 = division_bin(a, this_power)[0]

        b11 = modulo_bin(a2)
        b12 = xor_bin(b11, '1')
        c2 = division_bin(a2, power_bin(b12))[0]
        b14 = xor_bin(b12, '101')
        b51 = xor_bin(b14, c2)

        last_32 = modulo_bin(b51)
        if to_int(last_32) == 4:
            this_power = '1000'
            a3 = division_bin(a2, this_power)[0]

            b21 = modulo_bin(a3)
            # b11_int = to_int(b11)

            b22 = xor_bin(b21, '1')
            # b12_int = to_int(b12)

            div22 = power_bin(b22)
            # div2_int = to_int(div2)

            c3 = division_bin(a3, div22)[0]
            # c2_int = to_int(c2)

            b24 = xor_bin(b22, '101')
            # b4_int = to_int(b4)

            b521 = xor_bin(b24, c3)

            last_322 = modulo_bin(b521)
            if to_int(last_322) == 1:
                all_options.append(a)
                # this_power = '1000'
                # a4 = division_bin(a3, this_power)[0]
                #
                # b31 = modulo_bin(a4)
                # # b11_int = to_int(b11)
                #
                # b32 = xor_bin(b31, '1')
                # # b12_int = to_int(b12)
                #
                # div22 = power_bin(b32)
                # # div2_int = to_int(div2)
                #
                # c4 = division_bin(a4, div22)[0]
                # # c2_int = to_int(c2)
                #
                # b34 = xor_bin(b32, '101')
                # # b4_int = to_int(b4)
                #
                # b521 = xor_bin(b24, c4)
                #
                # last_3221 = modulo_bin(b521)
                # if to_int(last_3221) == 1:
                #     all_options.append(a)

ALL_A_ENDINGS = set([x[-STR_LNGTH:] for x in all_options])
ALL_A_ENDINGS = sorted(ALL_A_ENDINGS, key=lambda x: int(x, 2))
print('finished pre-processing')
print(len(ALL_A_ENDINGS))

# STR_LNGTH = 13
# ALL_A_ENDINGS = ['0000000000110', '0000000100010', '0000000100110', '0000001000110', '0000001001111', '0000001100010',
#                  '0000001100110', '0000100100010', '0001001001111', '0001001100010', '0001100100010', '0010000000110',
#                  '0010000100010', '0010000100110', '0010001000110', '0010001001111', '0010001100010', '0010001100110',
#                  '0010001100111', '0010010100010', '0010100100010', '0011000111101', '0011001001111', '0011001100010',
#                  '0011010111101', '0011100100010', '0100000000110', '0100000100010', '0100000100110', '0100001000110',
#                  '0100001001111', '0100001100010', '0100001100110', '0101001001111', '0101001100010', '0110000000110',
#                  '0110000100010', '0110000100110', '0110001000110', '0110001001111', '0110001100010', '0110001100110',
#                  '0110001100111', '0111000111101', '0111001001111', '0111001100010', '0111001111111', '0111010111101',
#                  '1000000000110', '1000000100010', '1000000100110', '1000001000110', '1000001001111', '1000001100010',
#                  '1000001100110', '1000111100010', '1001001001111', '1001001100010', '1001111100010', '1010000000110',
#                  '1010000100010', '1010000100110', '1010001000110', '1010001001111', '1010001100010', '1010001100110',
#                  '1010001100111', '1010010100010', '1010101100010', '1010111100010', '1011000111101', '1011001001111',
#                  '1011001100010', '1011010111101', '1011101100010', '1011111100010', '1100000000110', '1100000100010',
#                  '1100000100110', '1100001000110', '1100001001111', '1100001100010', '1100001100110', '1100001110111',
#                  '1100111100010', '1101001001111', '1101001100010', '1101001110111', '1101111100010', '1110000000110',
#                  '1110000100010', '1110000100110', '1110001000110', '1110001001111', '1110001100010', '1110001100110',
#                  '1110001100111', '1110111100010', '1111000111101', '1111001001111', '1111001100010', '1111001111111',
#                  '1111010111101', '1111111100010']
