from typing import Dict, Tuple


def read_all(file_name: str) -> Tuple[Dict[str, int], Dict[str, str]]:
    simple_inputs: Dict[str, int] = {}

    with open(file_name, "r") as file:
        lines = file.readlines()

        while True:
            line = lines.pop(0).rstrip()
            if line:
                split_line = line.split(': ')
                simple_inputs[split_line[0]] = int(split_line[1])

            else:
                break

        complex_inputs = {}
        while len(lines) > 0:
            line = lines.pop(0).rstrip()

            split_line = line.split(' -> ')

            complex_inputs[split_line[1]] = split_line[0]

    return simple_inputs, complex_inputs


class BinarySolver:
    def __init__(self,
                 simple_inputs: Dict[str, int],
                 complex_inputs: Dict[str, str]
                 ):
        self.simple_inputs = simple_inputs
        self.complex_inputs = complex_inputs

    def _value_of(self,
                  key: str
                  ) -> int:
        if key in self.simple_inputs:
            return self.simple_inputs[key]
        else:
            return self._solve_complex(key)

    def _solve_complex(
            self,
            key: str,
    ) -> int:
        complex_formula = self.complex_inputs.get(key, '')
        if complex_formula == '':
            print('ALARMOOOOO')
            return -1

        operand1 = complex_formula.split(' ')[0]
        operand2 = complex_formula.split(' ')[-1]

        value_of_1 = self._value_of(operand1)
        value_of_2 = self._value_of(operand2)

        operation_text = complex_formula.split(' ')[1]
        if operation_text.startswith('AND'):
            output = value_of_1 & value_of_2
        elif operation_text.startswith('XOR'):
            output = value_of_1 ^ value_of_2
        else:
            output = value_of_1 | value_of_2

        del self.complex_inputs[key]
        self.simple_inputs[key] = output

        return output

    def solve(self) -> str:
        output = {}
        for x in [x for x in c.keys() if x[0] == 'z']:
            this_outcome = self._solve_complex(x)
            output[x] = this_outcome

        output = {key.lstrip('z'): val for key, val in output.items()}
        sorted_values = [output[k] for k in sorted(output.keys(), reverse=True)]

        return ''.join(map(str, sorted_values))


def to_int(bin_str: str) -> int:
    return int(bin_str, 2)


s, c = read_all('data/task1.txt')

print(s)
print(c)

bs = BinarySolver(
    s,
    c
)

solution = bs.solve()
print(solution)
print(to_int(solution))
