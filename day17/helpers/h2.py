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


LNGTH_P = 14
STR_LNGTH = 7

all_options = []

all_possible_a_endings = [format(i, '03b') for i in range(2 ** LNGTH_P)]
all_possible_a_endings = [x.zfill(LNGTH_P) for x in all_possible_a_endings]
all_possible_a_endings = list(set(all_possible_a_endings))
print(len(all_possible_a_endings))

# i = 1
while len(all_possible_a_endings) > 0:
    a = all_possible_a_endings.pop()
    # a = '100000000000000000000000000010011111111111100010'

    b = modulo_bin(a)
    b = xor_bin(b, '1')
    c = division_bin(a, power_bin(b))[0]
    b = xor_bin(b, '101')
    b = xor_bin(b, c)

    last_3 = modulo_bin(b)
    if to_int(last_3) == 2:
        all_options.append(a)
        # a2 = division_bin(a, power_bin('1000'))[0]
        #
        # b = modulo_bin(a2)
        # b = xor_bin(b, '1')
        # c = division_bin(a2, power_bin(b))[0]
        # b = xor_bin(b, '101')
        # b = xor_bin(b, c)
        #
        # last_3 = modulo_bin(b)
        # if to_int(last_3) == 4:
        #     all_options.append(a)
            # a3 = division_bin(a,  power_bin('1000'))[0]
            #
            # b = modulo_bin(a3)
            # b = xor_bin(b, '1')
            # c = division_bin(a3, power_bin(b))[0]
            # b = xor_bin(b, '101')
            # b = xor_bin(b, c)
            #
            # last_3 = modulo_bin(b)
            # if to_int(last_3) == 1:
            #     all_options.append(a)
        #         a3 = division_bin(a3,  power_bin('1000'))[0]
        #
        #         b = modulo_bin(a3)
        #         b = xor_bin(b, '1')
        #         c = division_bin(a3, power_bin(b))[0]
        #         b = xor_bin(b, '101')
        #         b = xor_bin(b, c)
        #
        #         last_3 = modulo_bin(b)
        #         if to_int(last_3) == 1:
        #             # all_options.append(a)
        #             a3 = division_bin(a3,  power_bin('1000'))[0]
        #
        #             b = modulo_bin(a3)
        #             b = xor_bin(b, '1')
        #             c = division_bin(a3, power_bin(b))[0]
        #             b = xor_bin(b, '101')
        #             b = xor_bin(b, c)
        #
        #             last_3 = modulo_bin(b)
        #             if to_int(last_3) == 7:
        #                 all_options.append(a)


ALL_A_ENDINGS = set([x[-STR_LNGTH:] for x in all_options])
ALL_A_ENDINGS = sorted(ALL_A_ENDINGS, key=lambda x: int(x, 2))
print('finished pre-processing')
print(len(ALL_A_ENDINGS))

