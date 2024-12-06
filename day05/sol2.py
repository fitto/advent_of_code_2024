from typing import List, Dict


def read_rules_file(file_name: str) -> Dict[str, List[str]]:
    page_ordering_rules = {}

    with open(file_name, "r") as file:
        while True:
            line = file.readline()
            if not line:  # This means EOF (End of File) has been reached
                break
            if line == '\n':  # This line is empty
                break
            else:
                # print(line.rstrip())
                split_text = line.rstrip().split('|')
                page_ordering_rules.setdefault(split_text[0], []).append(split_text[1])
                # print(page_ordering_rules)
    return page_ordering_rules


def read_updates_file(file_name: str) -> List[List[str]]:
    output = []

    with open(file_name, "r") as file:
        for line in file:
            output.append(line.rstrip().split(','))

    return output


def check_updates(rules: Dict[str, List[str]],
                  updates: List[List[str]]
                  ) -> List[List[str]]:
    incorrect_rows = []

    for update in updates:
        check_outcome = check_row(rules, update)
        if not check_outcome:
            incorrect_rows.append(update)

    # print(incorrect_rows)
    return incorrect_rows


def check_row(rules: Dict[str, List[str]],
              update: List[str]
              ) -> bool:
    for i in range(len(update)):
        # print(update)
        this_number = update[i]
        dependencies = rules.get(this_number, [])

        for j in range(0, i):
            earlier_number = update[j]
            if earlier_number in dependencies:
                return False

        for j in range(i + 1, len(update)):
            checked_number = update[j]
            if checked_number not in dependencies:
                return False

    return True


def fix_lines(rules: Dict[str, List[str]],
              lines: List[List[str]]):
    output = []
    for line in lines:
        output.append(fix_line(rules, line))

    return output


def fix_line(rules: Dict[str, List[str]],
             update: List[str]) -> List[str]:
    print(f'attempting to fix {update}')
    while not check_row(rules, update):
        update = fix_char(rules, update)

    return update


def fix_char(rules: Dict[str, List[str]],
             update: List[str]) -> List[str]:
    for i in range(len(update)):
        # print(update)
        this_number = update[i]
        dependencies = rules.get(this_number, [])

        for j in range(0, i):
            earlier_number = update[j]
            if earlier_number in dependencies:
                return move_element(update, j, i + 1)

    return update


def move_element(lst, i, j):
    new_list = lst.copy()
    element_to_move = new_list.pop(i)
    new_list.insert(j + 1, element_to_move)

    return new_list


def calculate_output(list_of_strings: List[List[str]]):
    output = 0

    for val in list_of_strings:
        output += int(val[len(val) // 2])

    return output


# x = read_rules_file('data/test1_rules.txt')
# y = read_updates_file('data/test1_data.txt')
x = read_rules_file('data/task1_rules.txt')
y = read_updates_file('data/task1_data.txt')

z = check_updates(x, y)

w = fix_lines(x, z)
print(w)


print('ssssssssssssssss')
o = calculate_output(w)
print(o)
