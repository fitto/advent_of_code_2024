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
    correct_rows = []

    for update in updates:
        check_outcome = check_row(rules, update)
        if check_outcome:
            correct_rows.append(update)

    print(correct_rows)
    return correct_rows


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

o = calculate_output(z)
print(o)

# x = read_file('data/task1.txt')

# page ordering rules
# updates
