from typing import List


class ReadResult:
    def __init__(self, left_number: int,
                 right_numbers: List[int]
                 ):
        self.left_number = left_number
        self.right_numbers = right_numbers

    def __repr__(self):
        return f"NumberContainer(left_number={self.left_number}, right_numbers={self.right_numbers})"


def read_file(file_name: str) -> List[ReadResult]:
    output = []

    with open(file_name, "r") as file:
        for line in file:
            left_and_right = line.rstrip().split(': ')

            output.append(
                ReadResult(left_number=int(left_and_right[0]),
                           right_numbers=[int(itm) for itm in left_and_right[1].split(' ')]))

    return output


def analyze_item(left: int,
                 current_outcome: int,
                 right: List[int]
                 ) -> bool:
    if current_outcome == left and len(right) == 0:
        # print('***********************')
        return True
    elif current_outcome > left:
        # print('----------------')
        return False

    if len(right) == 0:
        # print('----------------')
        return False

    next_item = right[0]
    new_list = right[1:]

    # print(current_outcome)
    # print('add')
    # print(next_item)
    # print(add(current_outcome, next_item))

    add_outcome_result = analyze_item(
        left,
        add(current_outcome, next_item),
        new_list
    )

    if add_outcome_result:
        return add_outcome_result
    else:
        # print(current_outcome)
        # print('multiply')
        # print(next_item)
        # print(multiply(current_outcome, next_item))

        analyze_item_output = analyze_item(
            left,
            multiply(current_outcome, next_item),
            new_list
        )

        if analyze_item_output:
            return analyze_item_output
        else:
            return analyze_item(
                left,
                combine(current_outcome, next_item),
                new_list
            )


def add(a: int, b: int) -> int:
    return a + b


def multiply(a: int, b: int) -> int:
    return a * b


def combine(a: int, b: int) -> int:
    return int(str(a) + str(b))


# read_file_data = read_file('data/test1.txt')
read_file_data = read_file('data/task1.txt')

sum_keys = 0

for read_result in read_file_data:
    # print(key)
    # print('=======')
    otucome = analyze_item(read_result.left_number, read_result.right_numbers[0], read_result.right_numbers[1:])

    if otucome:
        sum_keys += read_result.left_number
print(sum_keys)

# --1038838603451
# --1038838603811
