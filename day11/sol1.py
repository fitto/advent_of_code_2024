def rule1(stone: str) -> list[str] | None:
    if stone == '0':
        return ['1']
    else:
        return None


def rule2(stone: str) -> list[str] | None:
    stone_digits_length = len(stone)

    if stone_digits_length % 2 == 0:
        half = int(stone_digits_length / 2)
        first_part = stone[:half]
        second_part = stone[half:]
        second_part = int(second_part)

        return [first_part, str(second_part)]
    else:
        return None


def rule3(stone: str) -> list[str]:
    return [str(int(stone) * 2024)]


def read_file(file_name: str) -> list[str]:
    text_table = []

    with open(file_name, "r") as file:
        for line in file:
            line_v = line.rstrip()

            text_table = text_table + line_v.split(' ')

    return text_table


def do_blinking(blinks: int,
                input_table: list[str]
                ):
    this_table = [x for x in input_table]

    for i in range(blinks):
        this_table = blink(this_table)
        print(i)
    print(len(this_table))


def blink(input_table: list[str]) -> list[str]:
    new_table = []
    for i in range(len(input_table)):
        this_number = input_table[i]

        r = rule1(this_number)
        if r is not None:
            new_table = new_table + r
        else:
            r = rule2(this_number)
            if r is not None:
                new_table = new_table + r

            else:
                new_table = new_table + rule3(this_number)

    return new_table


# read_file_data = read_file('data/1/22.txt')
read_file_data = read_file('data/task1.txt')
print(read_file_data)

do_blinking(75,
            read_file_data
            )
