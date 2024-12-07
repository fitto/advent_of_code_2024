def read_file(file_name: str) -> List[str]:
    pattern = r'mul\(\d{1,3},\d{1,3}\)'

    with open(file_name, "r") as file:
        for line in file:
            print(line)
            matches = re.findall(pattern, line.rstrip())

    return matches
