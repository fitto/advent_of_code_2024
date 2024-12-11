import math
import time


def read_file(file_name: str) -> list[str]:
    text_table = []

    with open(file_name, "r") as file:
        for line in file:
            line_v = line.rstrip()

            text_table = text_table + line_v.split(' ')

    return text_table


MEMORY = {}


def blink(stone, blink_times) -> int:
    if (stone, blink_times) in MEMORY.keys():
        return MEMORY[(stone, blink_times)]
    else:
        if blink_times == 0:
            return 1

        else:
            if stone == 0:  # Rule 1
                # print(f'Calling 1 {stone}/{blink_times - 1}')
                return blink(1, blink_times - 1)
            else:
                lngth = int(math.log10(stone)) + 1
                if lngth % 2 == 0:  # Rule 2
                    a = 10 ** (lngth // 2)
                    o1 = stone // a
                    o2 = stone % a

                    # print(f'Calling 2a {o1}/{blink_times - 1}')
                    # print(f'Calling 2b {o2}/{blink_times - 1}')
                    both = blink(o1, blink_times - 1) + blink(o2, blink_times - 1)
                else:
                    # print(f'Calling 3 {stone * 2024}/{blink_times - 1}')
                    return blink(stone * 2024, blink_times - 1)

        MEMORY[(stone, blink_times)] = both
        return both


start = time.time()
# data = read_file('data/1/22.txt')
data = read_file('data/task1.txt')
data = [int(a) for a in data]

output = 0
for this_stone in data:
    output += blink(this_stone, 75)

print(output)
end = time.time()
print(f"Execution time: {end - start:.6f} seconds")
