from typing import Tuple



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



last_6_of_a = [format(i, '03b') for i in range(2 ** 6)]
last_6_of_a = [x.zfill(6) for x in last_6_of_a]
print(len(last_6_of_a))

last_3_of_a = set([binary[-3:] for binary in last_6_of_a])
print(len(last_3_of_a))

digits_6_3_a = set([binary[-6:-3] for binary in last_6_of_a])
print(len(digits_6_3_a))


# STEP 1
bs = [x for x in last_3_of_a]


# STEP 2
# •	1 -> 1 ->
# o	Sets B to b XOR ‘101’
bs = [xor_bin(b, '001') for b in bs]

print(bs)

# # STEP 3
# # •	7 -> 5 -> modifies C
# # o	divisision A / 2^B
# cs = [division_bin(a,  power_bin(b))[0] for b in step_2_output]
# print(cs)
#
# # STEP 4
# # •	1 -> 5 -> modifies B
# step_4_output = [xor_bin(b, '101') for b in bs]
# print(f'step_1_output {step_2_output}')
#
# # STEP 5
# # •	4 -> 0
# step_4_output = [xor_bin(b, '101') for b in bs]
# print(f'step_1_output {step_2_output}')