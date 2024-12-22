from keypad_solver import KeypadSolver

DEBUG = False

ROBOTS = 25

this_task = [
    '463A',
    '340A',
    '129A',
    '083A',
    '341A'
]
#
# this_task = ['029A',
#         '463A',
#         '340A'
#         ]
ks = KeypadSolver(debug=DEBUG)

solved = ks.solve(this_task, ROBOTS)

output = 0
for key, val in solved.items():
    numeric_part = int(key[:-1])
    output += val * numeric_part
print(output)