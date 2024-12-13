from dataclasses import dataclass
from typing import List

from sympy import symbols, Eq, solve, Integer

from day13.objects.button import Button
from day13.objects.prize import Prize


@dataclass(frozen=True)
class GameOption:
    button_a: Button
    button_b: Button
    prize: Prize
    button_a_cost: int = 3
    button_b_cost: int = 1

    def __post_init__(self):
        # Convert list to tuple to make it hashable
        x = 10000000000000
        object.__setattr__(self, 'prize', Prize(self.prize.x_val + x, self.prize.y_val + x))

    @staticmethod
    def from_str(text_lines: List[str]):
        return GameOption(
            Button.from_str(text_lines[0].rstrip()),
            Button.from_str(text_lines[1].rstrip()),
            Prize.from_str(text_lines[2].rstrip())
        )

    def solve_option(self):
        x, y = symbols('x y')

        # Define the coefficients and constants
        a1, b1, p1 = self.button_a.x_move, self.button_b.x_move, self.prize.x_val
        a2, b2, p2 = self.button_a.y_move, self.button_b.y_move, self.prize.y_val

        # Define the equations
        equation1 = Eq(a1 * x + b1 * y, p1)
        equation2 = Eq(a2 * x + b2 * y, p2)

        # Solve the system of equations
        solution = solve((equation1, equation2), (x, y))

        # if isinstance(solution[x], Rational) and isinstance(solution[y], Rational):
        #     print(solution[x], solution[y])
        #     return None

        if isinstance(solution[x], Integer) and isinstance(solution[y], Integer):
            return solution[x], solution[y]
        else:
            print(solution)
            return None

    def solution_cost(self):
        sol = self.solve_option()
        if sol is None:
            return None
        # elif sol[0] > 100 or  sol[1] > 100:
        #     return None
        else:
            return sol[0] * self.button_a_cost + sol[1] * self.button_b_cost

    # def _solve_from(self, a_pushed: int, b_pushed: int):
    #     x_sum = a_pushed * self.button_a.x_move + b_pushed * self.button_b.x_move
    #     y_sum = a_pushed * self.button_a.y_move + b_pushed * self.button_b.y_move
    #
    #     if x_sum > self.prize.x_val or y_sum > self.prize.y_val:
    #         return None
    #
    #     # print(f'{a_pushed} / {b_pushed} = {x_sum} {y_sum}')
    #     # print('pusing a')
    #     a_outcome = self._solve_from(a_pushed + 1, b_pushed)
    #     if a_outcome is not None:
    #         return a_pushed, b_pushed
    #     else:
    #         # print('pusing b')
    #         return self._solve_from(a_pushed, b_pushed + 1)
