"""
--- Part Two ---
The engineer finds the missing part and installs it in the engine! As the
engine springs to life, you jump in the closest gondola, finally ready to
ascend to the water source.

You don't seem to be going very fast, though. Maybe something is still wrong?
Fortunately, the gondola has a phone labeled "help", so you pick it up and the
engineer answers.

Before you can explain the situation, she suggests that you look out the
window. There stands the engineer, holding a phone in one hand and waving with
the other. You're going so slowly that you haven't even left the station. You
exit the gondola.

The missing part wasn't the only issue - one of the gears in the engine is
wrong. A gear is any * symbol that is adjacent to exactly two part numbers. Its
gear ratio is the result of multiplying those two numbers together.

This time, you need to find the gear ratio of every gear and add them all up so
that the engineer can figure out which gear needs to be replaced.

Consider the same engine schematic again:
    467..114..
    ...*......
    ..35..633.
    ......#...
    617*......
    .....+.58.
    ..592.....
    ......755.
    ...$.*....
    .664.598..
In this schematic, there are two gears. The first is in the top left; it has
part numbers 467 and 35, so its gear ratio is 16345. The second gear is in the
lower right; its gear ratio is 451490. (The * adjacent to 617 is not a gear
because it is only adjacent to one part number.) Adding up all of the gear
ratios produces 467835.

What is the sum of all of the gear ratios in your engine schematic?
"""
from typing import Optional

def task(schematic_lines: list[str]) -> list[int]:
    """ Solves the task. """
    def is_gear_cell(cell: str) -> bool:
        """ Returns true if given cell is a gear. """
        return cell == '*'

    def get_gear_pos_end(schematic_lines, i_middle, j) -> Optional[tuple[int, int]]:
        """ Returns the gear position if there is a part in row :i_middle + [-1, 0, +1] and :jth column. """
        # check top-diagonal
        if i_middle > 0:
            if is_gear_cell(schematic_lines[i_middle - 1][j]):
                return (i_middle - 1, j)
        # check horizontally adjacent
        if is_gear_cell(schematic_lines[i_middle][j]):
            return (i_middle, j)
        # check bottom-diagonal
        if i_middle < len(schematic_lines[i]) - 1:
            if is_gear_cell(schematic_lines[i_middle + 1][j]):
                return (i_middle + 1, j)

        return None

    gear_numbers = {}
    for i, line in enumerate(schematic_lines):
        num_buffer = ''
        adjacent_gear_pos = None
        for j, c in enumerate(line):
            # Part adjacency checks:
            # - for the all numbers:  top, bottom
            # - for the first number: top-left, left, bottom-left
            # - for the last number:  top-right, right, bottom-right

            if c.isnumeric():
                if len(num_buffer) == 0:
                    # first number -> check left
                    if adjacent_gear_pos is None and j > 0:
                        adjacent_gear_pos = get_gear_pos_end(schematic_lines, i, j - 1)
                        print(c, 'left', adjacent_gear_pos)

                # check top
                if adjacent_gear_pos is None and i > 0:
                    if is_gear_cell(schematic_lines[i - 1][j]):
                        adjacent_gear_pos = (i - 1, j)
                        print(c, 'top', adjacent_gear_pos)

                # check bottom
                if adjacent_gear_pos is None and i < len(schematic_lines) - 1:
                    if is_gear_cell(schematic_lines[i + 1][j]):
                        adjacent_gear_pos = (i + 1, j)
                        print(c, 'bottom', adjacent_gear_pos)

                num_buffer += c

            # number ended -> commit
            elif len(num_buffer) > 0:
                # last number -> check right
                if not adjacent_gear_pos and j < len(schematic_lines[i]):
                    adjacent_gear_pos = get_gear_pos_end(schematic_lines, i, j)
                    print(line[j - 1], 'right', adjacent_gear_pos)

                if adjacent_gear_pos is not None:
                    gear_numbers.setdefault(adjacent_gear_pos, []).append(int(num_buffer))
                num_buffer = ''
                adjacent_gear_pos = None

        # line and number ended -> commit
        if len(num_buffer) > 0:
            if adjacent_gear_pos is not None:
                gear_numbers.setdefault(adjacent_gear_pos, []).append(int(num_buffer))

    gear_ratios = []
    for n in gear_numbers.values():
        if len(n) == 2:
            gear_ratios.append(n[0] * n[1])

    return gear_ratios

with open('input.txt', 'r', encoding='ascii') as f:
   input_lines = [l.strip() for l in f.readlines()]

gear_ratios = task(input_lines)

print( sum(gear_ratios) )
