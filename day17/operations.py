from typing import Tuple, Dict, List, Optional


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


class ProgramSolver:
    def __init__(self,
                 initial_register: Dict[str, str],
                 this_program_input_bin: List[str]
                 ):
        self.this_register_bin = initial_register
        self.this_program_input_bin = this_program_input_bin

    def get_combo_operand_bin(self, input_operand_bin: str) -> str:
        if input_operand_bin == '100':
            return self.this_register_bin['A']
        elif input_operand_bin == '101':
            return self.this_register_bin['B']
        elif input_operand_bin == '110':
            return self.this_register_bin['C']
        else:
            as_int = to_int(input_operand_bin)
            if as_int > 3 or as_int < 0:
                print(f'input_operand_bin {input_operand_bin} which is {as_int}')
            return input_operand_bin

    def solve(self) -> List[str]:
        output_bin = []
        instruction_pointer = 0

        while True:
            if instruction_pointer < len(self.this_program_input_bin):

                instruction_number = to_int(self.this_program_input_bin[instruction_pointer])
                operand_as_bit = self.this_program_input_bin[instruction_pointer + 1]

                # adv
                if instruction_number == 0:
                    self.this_register_bin['A'] = \
                        division_bin(self.this_register_bin['A'],
                                     power_bin(self.get_combo_operand_bin(operand_as_bit)))[0]
                    instruction_pointer += 2
                    # print(f' a {this_register_bin['A']}')

                # bxl
                elif instruction_number == 1:
                    self.this_register_bin['B'] = xor_bin(self.this_register_bin['B'], operand_as_bit)
                    instruction_pointer += 2

                # bst
                elif instruction_number == 2:
                    self.this_register_bin['B'] = modulo_bin(self.get_combo_operand_bin(operand_as_bit))
                    instruction_pointer += 2

                # jnz
                elif instruction_number == 3:
                    if is_binary_zero(self.this_register_bin['A']):
                        instruction_pointer += 2
                    else:
                        instruction_pointer = to_int(operand_as_bit)

                # bxc
                elif instruction_number == 4:
                    self.this_register_bin['B'] = xor_bin(self.this_register_bin['B'], self.this_register_bin['C'])
                    instruction_pointer += 2

                # out
                elif instruction_number == 5:
                    output_bin.append(modulo_bin(self.get_combo_operand_bin(operand_as_bit)))
                    instruction_pointer += 2

                # bdv
                elif instruction_number == 6:
                    self.this_register_bin['B'] = \
                        division_bin(self.this_register_bin['A'],
                                     power_bin(self.get_combo_operand_bin(operand_as_bit)))[0]

                    instruction_pointer += 2

                # cdv
                elif instruction_number == 7:
                    self.this_register_bin['C'] = \
                        division_bin(self.this_register_bin['A'],
                                     power_bin(self.get_combo_operand_bin(operand_as_bit)))[0]

                    instruction_pointer += 2
                else:
                    print(f'ARALRMO {instruction_number}')
            else:
                break

        return output_bin

    def solve_n_first(self,
                      n: int
                      ) -> Optional[List[str]]:
        output_bin = []
        instruction_pointer = 0

        while True:
            if instruction_pointer < len(self.this_program_input_bin):

                instruction_number = to_int(self.this_program_input_bin[instruction_pointer])
                operand_as_bit = self.this_program_input_bin[instruction_pointer + 1]

                # adv
                if instruction_number == 0:
                    self.this_register_bin['A'] = \
                        division_bin(self.this_register_bin['A'],
                                     power_bin(self.get_combo_operand_bin(operand_as_bit)))[0]
                    instruction_pointer += 2
                    # print(f' a {this_register_bin['A']}')

                # bxl
                elif instruction_number == 1:
                    self.this_register_bin['B'] = xor_bin(self.this_register_bin['B'], operand_as_bit)
                    instruction_pointer += 2

                # bst
                elif instruction_number == 2:
                    self.this_register_bin['B'] = modulo_bin(self.get_combo_operand_bin(operand_as_bit))
                    instruction_pointer += 2

                # jnz
                elif instruction_number == 3:
                    if is_binary_zero(self.this_register_bin['A']):
                        instruction_pointer += 2
                    else:
                        instruction_pointer = to_int(operand_as_bit)

                # bxc
                elif instruction_number == 4:
                    self.this_register_bin['B'] = xor_bin(self.this_register_bin['B'], self.this_register_bin['C'])
                    instruction_pointer += 2

                # out
                elif instruction_number == 5:
                    output_bin.append(modulo_bin(self.get_combo_operand_bin(operand_as_bit)))

                    if len(output_bin) >= n:
                        return output_bin

                    instruction_pointer += 2

                # bdv
                elif instruction_number == 6:
                    self.this_register_bin['B'] = \
                        division_bin(self.this_register_bin['A'],
                                     power_bin(self.get_combo_operand_bin(operand_as_bit)))[0]

                    instruction_pointer += 2

                # cdv
                elif instruction_number == 7:
                    self.this_register_bin['C'] = \
                        division_bin(self.this_register_bin['A'],
                                     power_bin(self.get_combo_operand_bin(operand_as_bit)))[0]

                    instruction_pointer += 2
                else:
                    print(f'ARALRMO {instruction_number}')
            else:
                break

        return output_bin

    def solve_with_a(self,
                     a: str
                     ) -> List[str]:
        self.this_register_bin['A'] = a
        return self.solve()
