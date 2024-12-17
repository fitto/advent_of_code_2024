# from typing import Tuple
#
#
# def to_bin(number: int) -> str:
#     return bin(number)[2:]
#
#
# def to_int(bin_str: str) -> int:
#     return int(bin_str, 2)
#
#
# def division_bin(dividend, divisor) -> Tuple[str, str]:
#     # Initialize quotient and remainder as strings
#     quotient = ''
#     remainder = ''
#
#     # Precompute divisor length and integer value
#     divisor_len = len(divisor)
#     divisor_int = int(divisor, 2)
#
#     for bit in dividend:
#         # Shift left by appending current bit to remainder
#         remainder += bit
#
#         # Remove leading zeros from remainder
#         remainder = remainder.lstrip('0')
#
#         # Compare remainder with divisor
#         if len(remainder) >= divisor_len and int(remainder, 2) >= divisor_int:
#             # Subtract divisor from remainder
#             temp_remainder = int(remainder, 2) - divisor_int
#             remainder = bin(temp_remainder)[2:]
#             quotient += '1'
#         else:
#             quotient += '0'
#
#     quotient_output = quotient.lstrip('0')
#     if len(quotient_output) == 0:
#         quotient_output = '0'
#
#     return quotient_output, remainder
#
#
# def modulo_bin(binary_string: str) -> str:
#     # Initialize remainder as a binary string
#     remainder = '0'
#
#     if len(binary_string) == 0:
#         binary_string = '0'
#
#     # Iterate over each bit in the binary string
#     for bit in binary_string:
#         # Update remainder for each bit
#         # Convert remainder to integer, perform modulo, and convert back to binary
#         remainder = bin((int(remainder, 2) * 2 + int(bit)) % 8)[2:]
#
#     # Ensure the remainder is represented as a binary string
#     return remainder  # Pad with leading zeros to
#
#
# def power_bin(bin_num) -> str:
#     # Initialize the decimal value of bin_num
#     decimal_value = 0
#
#     # Calculate the decimal value of bin_num without direct conversion
#     for bit in bin_num:
#         decimal_value = decimal_value * 2 + int(bit)
#
#     # Compute 2^decimal_value in binary by shifting '1' left
#     result = '1' + '0' * decimal_value
#
#     return result
#
#
# def xor_bin(bin1, bin2) -> str:
#     # Pad the shorter string with leading zeros
#     max_len = max(len(bin1), len(bin2))
#     bin1 = bin1.zfill(max_len)
#     bin2 = bin2.zfill(max_len)
#
#     # Perform XOR operation bit by bit
#     result = []
#     for b1, b2 in zip(bin1, bin2):
#         # XOR operation: 1 if bits are different, 0 if they are the same
#         result.append('1' if b1 != b2 else '0')
#
#     output = ''.join(result)
#     if len(output) == 0:
#         return '0'
#
#     # Join the result list to form the final binary string
#     return output
#
#
# def is_binary_zero(binary_string) -> bool:
#     return binary_string.strip('0') == ''
#
#
# all_options = []
#
# all_possible_a_endings = [format(i, '03b') for i in range(2 ** 12)]
# # all_possible_a_endings = ['00000110', '00001110', '00010110', '00011110', '00100010', '00100110', '00101110', '00110101', '00110110', '00111101', '00111110', '01000100', '01000110', '01000111', '01001100', '01001110', '01001111', '01010100', '01010110', '01010111', '01011100', '01011110', '01011111', '01100010', '01100110', '01100111', '01101110', '01101111', '01110110', '01110111', '01111110', '01111111', '10100010', '10110101', '10111101', '11100010']
# print(len(all_possible_a_endings))
# all_possible_a_endings = [x.zfill(10) for x in all_possible_a_endings]
# all_possible_a_endings = list(set(all_possible_a_endings))
# print(len(all_possible_a_endings))
#
# # i = 1
# while len(all_possible_a_endings) > 0:
#     a = all_possible_a_endings.pop()
#     b1 = modulo_bin(a)
#     b1_int = to_int(b1)
#
#     b2 = xor_bin(b1, '1')
#     b2_int = to_int(b2)
#
#     div = power_bin(b2)
#     div_int = to_int(div)
#
#     c = division_bin(a, div)[0]
#     c_int = to_int(c)
#
#     b4 = xor_bin(b2, '101')
#     b4_int = to_int(b4)
#
#     this_case = xor_bin(c, b4)
#     this_case_int = to_int(this_case)
#
#     last_3 = this_case[-3:]
#
#     if to_int(last_3) == 2:
#         # print(f'a={a}, b={b4}, c={c}')
#         all_options.append(a)
#
#     # i += 1
#     # if i % 1000 == 0:
#     #     print(len(all_possible_a_endings))
#
# # print(len(all_options))
# # print(len(set(all_options)))
# # print([x for x in set(all_options)])
#
# ALL_A_ENDINGS = set([x[-12:] for x in all_options])
# ALL_A_ENDINGS = sorted(ALL_A_ENDINGS, key=lambda x: int(x, 2))
# print('finished pre-processing')
# print(len(ALL_A_ENDINGS))
#
# # for x in ALL_A_ENDINGS:
# #     print(len(a))
# # print(len(ALL_A_ENDINGS))
