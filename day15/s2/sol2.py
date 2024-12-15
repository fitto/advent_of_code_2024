from typing import List

from day15.s2.domain.world import World


def read_file(file_name: str) -> List[List[str]]:
    output = []

    with open(file_name, 'r') as file:
        for line in file:
            line = line.rstrip()

            this_line = []
            for char in line:
                if char == '#':
                    this_line.append('#')
                    this_line.append('#')
                elif char == 'O':
                    this_line.append('[')
                    this_line.append(']')
                elif char == '.':
                    this_line.append('.')
                    this_line.append('.')
                elif char == '@':
                    this_line.append('@')
                    this_line.append('.')
                else:
                    print('WHOOPS')

            output.append(this_line)

    output[0] = output[0][:len(output[1])]
    output[len(output) - 1] = output[len(output) - 1][:len(output[1])]
    return output


new_input = read_file('data/21map.txt')
this_world = World.from_list(new_input)
this_world.visualize()


def do_moves(file_name: str, initial_world: World) -> World:
    wrld = initial_world

    with open(file_name, 'r') as file:
        # Read the file character by character
        for char in file.read():
            # Ignore newline characters
            if char != '\n':
                wrld = wrld.robot_move(char)
                print('')
                print('------------------')
                print('')
                print(f'MOVING: {char}')
                wrld.visualize()

    return wrld


end_world = do_moves('data/21moves.txt', this_world)
# end_world = do_moves('data/task1moves.txt', this_world)

# print(end_world.all_coordinates_value)
