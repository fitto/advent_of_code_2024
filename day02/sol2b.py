from typing import List


def read_and_process_file(file_name: str):
    with open(file_name, "r") as file:
        counter = 0

        for line in file:
            numbers = line.rstrip().split(' ')
            outcome = assess_line(numbers)

            if outcome[0]:
                counter += 1
                continue
            else:
                for i in range(3):
                    x = numbers.copy()
                    del x[outcome[1] - i]

                    outcome2 = assess_line(x)

                    if outcome2[0]:
                        print(line)
                        counter += 1
                        break

    return counter


def assess_line(numbers: List[str]) -> tuple[bool, int]:
    increasing = None

    i = 1
    while i < len(numbers):
        dist = int(numbers[i]) - int(numbers[i - 1])

        if abs(dist) > 3 or dist == 0:
            return False, i

        if increasing is None and dist > 0:
            increasing = True
        if increasing is None and dist < 0:
            increasing = False

        if (dist > 0 and not increasing) or (dist < 0 and increasing):
            return False, i

        i += 1
        if i == len(numbers):
            return True, -1


print(read_and_process_file('test1.txt'))
print(read_and_process_file('task1.txt'))
