from typing import Tuple, Dict

TEST_INPUTS = [
    1
    , 10
    , 100
    , 2024
]


class Solver:
    def __init__(self):
        self.MEMORY: Dict[Tuple[int, int], int] = {}

    def value_after(self,
                    input_number: int,
                    iteration_number: int
                    ) -> int:

        mem = self.MEMORY.get((input_number, iteration_number))
        if mem:
            return mem

        secret = input_number

        for i in range(1, iteration_number + 1):
            # Calculate the result of multiplying the secret number by 64
            result = secret * 64
            # Then, mix this result into the secret number
            secret = secret ^ result
            # Finally, prune the secret number.
            secret = secret % 16777216

            # Calculate the result of dividing the secret number by 32
            result2 = int(secret / 32)
            # Then, mix this result into the secret number
            secret = secret ^ result2
            # Finally, prune the secret number.
            secret = secret % 16777216

            # Calculate the result of multiplying the secret number by 2048
            result3 = secret * 2048
            # Then, mix this result into the secret number
            secret = secret ^ result3
            # Finally, prune the secret number.
            secret = secret % 16777216

            self.MEMORY[(input_number, iteration_number)] = secret

        return secret


def read_integers_from_file(file_path: str) -> list[int]:
    with open(file_path, 'r') as file:
        # Use list comprehension to read and convert each line to an integer
        integers = [int(line.strip()) for line in file]
    return integers


numbers_list = read_integers_from_file('data/task1.txt')

ITERS = 2000

output = 0
s = Solver()
for itm in numbers_list:
    # print(f'result for {itm} is {s.value_after(itm, ITERS)}')
    output += s.value_after(itm, ITERS)

print(output)
