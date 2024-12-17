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


binary_numbers = [format(i, '03b') for i in range(2 ** 3)]
print(binary_numbers)

bs = [format(i, '03b') for i in range(2 ** 3)]
cs = [format(i, '03b') for i in range(2 ** 3)]

for b in bs:
    for c in cs:
        if xor_bin(b, c) == '010':
            print(f'b={b}, c={c}')
