# KEYPAD_BIG = [
#     ['7', '8', '9'],
#     ['4', '5', '6'],
#     ['1', '2', '3'],
#     [' ', '0', 'A']
# ]
from day18.coordinates import Coordinates

KEYPAD_BIG = {
    '7': Coordinates(0, 0),
    '8': Coordinates(0, 1),
    '9': Coordinates(0, 2),
    '4': Coordinates(1, 0),
    '5': Coordinates(1, 1),
    '6': Coordinates(1, 2),
    '1': Coordinates(2, 0),
    '2': Coordinates(2, 1),
    '3': Coordinates(2, 2),
    '0': Coordinates(3, 1),
    'A': Coordinates(3, 2)
}

# KEYPAD_SMALL = [
#     [' ', '^', 'A'],
#     ['<', 'v', '>']
# ]


KEYPAD_SMALL = {
    '^': Coordinates(0, 1),
    'A': Coordinates(0, 2),
    '<': Coordinates(1, 0),
    'v': Coordinates(1, 1),
    '>': Coordinates(1, 2)
}