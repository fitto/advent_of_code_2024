from typing import Tuple, Dict, List, Set

# monkey_inputs = [
#     1
#     , 2
#     , 3
#     , 2024
# ]


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


class MonkeyBusiness:
    def __init__(self):
        self.prices = []
        # self.max_cache = None
        # self.max_price_occurences_cache = None
        self._price_changes_cache = None
        self._all_price_change_sequences_cache = None

    def add_price_from_number(self, number: int):
        self.prices.append(number % 10)

    @property
    def price_changes(self):
        if self._price_changes_cache is None:
            self._price_changes_cache = [self.prices[i + 1] - self.prices[i] for i in range(len(self.prices) - 1)]
        return self._price_changes_cache

    @property
    def all_price_change_sequences(self) -> Dict[Tuple[int, int, int, int], int]:
        if self._all_price_change_sequences_cache is None:
            this_dict = {}

            for i in range(len(self.price_changes) - 3):
                c1 = self.price_changes[i]
                c2 = self.price_changes[i + 1]
                c3 = self.price_changes[i + 2]
                c4 = self.price_changes[i + 3]

                check = this_dict.get((c1, c2, c3, c4))
                if check is None:
                    this_dict[(c1, c2, c3, c4)] = self.prices[i + 4]

            self._all_price_change_sequences_cache = this_dict

        return self._all_price_change_sequences_cache

    def price_after_four_changes(self, changes_sequence: Tuple[int, int, int, int]) -> int:

        return self.all_price_change_sequences.get(changes_sequence, 0)

    #
    # @property
    # def max_price(self) -> int:
    #     if self.max_cache is None:
    #         max_n = max(self.prices)
    #         self.max_cache = max_n
    #     return self.max_cache
    #
    # @property
    # def max_price_occurences(self):
    #     if self.max_price_occurences_cache is None:
    #         output = []
    #         for i in range(len(self.prices)):
    #             if self.prices[i] == self.max_price:
    #                 output.append(i)
    #         self.max_price_occurences_cache = output
    #     return self.max_price_occurences_cache
    #

    # def price_after_four_changes(self, i: int):
    #     return self.prices[i + 4]


def read_integers_from_file(file_path: str) -> list[int]:
    with open(file_path, 'r') as file:
        # Use list comprehension to read and convert each line to an integer
        integers = [int(line.strip()) for line in file]
    return integers


monkey_inputs = read_integers_from_file('data/task1.txt')


ITERS = 2000
monkey_businesses: List[MonkeyBusiness] = []

s = Solver()
print(f'creating prices')
mn = 1
for monkey_input in monkey_inputs:

    this_monkey = MonkeyBusiness()

    for i in range(ITERS):
        # print(f'result for {monkey_input} is {s.value_after(monkey_input, i)}')
        this_monkey.add_price_from_number(s.value_after(monkey_input, i))

    monkey_businesses.append(this_monkey)
    print(f'   added {mn} monkeys so far')
    mn += 1

print(f'getting all sequences')
all_four_sequences: Set[Tuple[int, int, int, int]] = set()
for m in monkey_businesses:
    all_four_sequences |= m.all_price_change_sequences.keys()

print(f'getting bes sequence')

best_result = 0
best_sequence = None
for price_changes_sequence in all_four_sequences:
    result_for_sequence = 0
    for m in monkey_businesses:
        result_for_sequence += m.price_after_four_changes(price_changes_sequence)
    if result_for_sequence > best_result:
        best_result = result_for_sequence
        best_sequence = price_changes_sequence

print(best_result)
print(best_sequence)
