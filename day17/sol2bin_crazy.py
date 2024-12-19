from typing import Any, List, Dict

from day17.operations import to_bin, ProgramSolver, to_int


def read_all(file_name: str) -> tuple[dict[str, str], list[Any] | list[str]]:
    registers = {}
    registers_bin = {}
    # program = []
    program_bin = []

    with open(file_name, "r") as file:
        lines = file.readlines()

        for line in lines:
            if line.startswith('Register '):
                reg = line.rstrip()[len('Register '):].strip()
                registers[reg[0]] = int(reg.split(' ')[1])
                registers_bin[reg[0]] = to_bin(registers[reg[0]])

            if line.startswith('Program: '):
                p = line.rstrip()[len('Program: '):].strip()
                program = p.split(',')
                program = [int(x) for x in program]
                program_bin = [to_bin(x) for x in program]

    # registers, program,
    return registers_bin, program_bin


def reverse_solve(expected_solution: List[int],
                  initial_register: Dict[str, str],
                  this_program_input_bin: List[str]
                  ) -> List[str]:
    s = ProgramSolver(initial_register, this_program_input_bin)

    options_to_check = [(0, '0'), (0, '1')]
    outputs = []

    while len(options_to_check) > 0:
        places_from_end, a_candidate = options_to_check.pop()
        if DEBUG:
            print(f'looking at {to_int(a_candidate)}')

        for i in range(8):
            i_bit = to_bin(i).zfill(3)
            a_cand = a_candidate + i_bit

            solution_bin = s.solve_with_a(a_cand)

            n_th_element = - places_from_end - 1
            # expected = expected_solution[n_th_element:]
            solution_bin_end = solution_bin[n_th_element:]
            expected_solution_end = expected_solution[n_th_element:]

            if solution_bin_end == expected_solution_end:
                # if DEBUG:
                # print(f'adding {(places_from_end + 1, a_cand)}')
                options_to_check.append((places_from_end + 1, a_cand))

                if len(solution_bin) == len(expected_solution):
                    outputs.append(a_cand)

            if places_from_end > len(expected_solution):
                if DEBUG:
                    print('breaking at ')
                break

    return outputs


DEBUG = False

this_register_bin, this_program_input_bin = read_all('data/task1.txt')
# this_register_bin, this_program_input_bin = read_all('data/11.txt')
sol_bin = reverse_solve(this_program_input_bin,
                        this_register_bin,
                        this_program_input_bin
                        )

sol_normal = [to_int(x) for x in sol_bin]
sol_normal = sorted(sol_normal)

if len(sol_normal) > 0:
    print(sol_normal[0])
else:
    print('No sol')

# s = ProgramSolver(this_register_bin, this_program_input_bin)
# solution_bin = s.solve()
# solution = [to_int(x) for x in solution_bin]
# print(solution_bin)
# print(solution)
