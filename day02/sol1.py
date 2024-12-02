def read_and_process_file(file_name: str) -> int:
    with open(file_name, "r") as file:

        counter = 0

        for line in file:
            numbers = line.rstrip().split(' ')

            # print(numbers)
            increasing = None

            i = 1
            while i < len(numbers):
                dist = int(numbers[i]) - int(numbers[i - 1])

                if abs(dist) > 3 or dist == 0:
                    break

                if increasing is None and dist > 0:
                    increasing = True
                if increasing is None and dist < 0:
                    increasing = False

                if (dist > 0 and not increasing) or (dist < 0 and increasing):
                    break

                i += 1
                if i == len(numbers):
                    # print(line)
                    counter += 1

    return counter


print(read_and_process_file('test1.txt'))
print(read_and_process_file('task1.txt'))
