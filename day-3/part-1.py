"""
--- Day 3: Gear Ratios ---

You and the Elf eventually reach a gondola lift station; he says the gondola
lift will take you up to the water source, but this is as far as he can bring
you. You go inside.

It doesn't take long to find the gondolas, but there seems to be a problem:
they're not moving.

"Aaah!"

You turn around to see a slightly-greasy Elf with a wrench and a look of
surprise. "Sorry, I wasn't expecting anyone! The gondola lift isn't working
right now; it'll still be a while before I can fix it." You offer to help.

The engineer explains that an engine part seems to be missing from the engine,
but nobody can figure out which one. If you can add up all the part numbers in
the engine schematic, it should be easy to work out which part is missing.

The engine schematic (your puzzle input) consists of a visual representation
of the engine. There are lots of numbers and symbols you don't really
understand, but apparently any number adjacent to a symbol, even diagonally,
is a "part number" and should be included in your sum. (Periods (.) do not
count as a symbol.)

Here is an example engine schematic:
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
In this schematic, two numbers are not part numbers because they are not
adjacent to a symbol: 114 (top right) and 58 (middle right). Every other
number is adjacent to a symbol and so is a part number; their sum is 4361.

Of course, the actual engine schematic is much larger. What is the sum of
all of the part numbers in the engine schematic?
"""
def task(schematic_lines: list[str]) -> list[int]:
    """ Solves the task. """
    def is_part_cell(cell: str) -> bool:
        """ Returns true if given cell is a part cell (not numeric and or a dot). """
        return not cell.isnumeric() and cell != '.'

    def has_parts_end(schematic_lines, i_middle, j) -> bool:
        """ Returns true if there is a part in row :i_middle + [-1, 0, +1] and :jth column. """
        # check top-diagonal
        if i_middle > 0:
            if is_part_cell(schematic_lines[i_middle - 1][j]):
                return True
        # check horizontally adjacent
        if is_part_cell(schematic_lines[i_middle][j]):
            return True
        # check bottom-diagonal
        if i_middle < len(schematic_lines[i]) - 1:
            if is_part_cell(schematic_lines[i_middle + 1][j]):
                return True

        return False

    part_numbers = []
    for i, line in enumerate(schematic_lines):
        num_buffer = ''
        has_adjacent_part = False
        for j, c in enumerate(line):
            # Part adjacency checks:
            # - for the all numbers:  top, bottom
            # - for the first number: top-left, left, bottom-left
            # - for the last number:  top-right, right, bottom-right

            if c.isnumeric():
                if len(num_buffer) == 0:
                    # first number -> check left
                    if not has_adjacent_part and j > 0:
                        has_adjacent_part = has_parts_end(schematic_lines, i, j - 1)
                        #print(c, 'left', has_adjacent_part)

                # check top
                if not has_adjacent_part and i > 0:
                    has_adjacent_part = is_part_cell(schematic_lines[i - 1][j])
                    #print(c, 'top', has_adjacent_part)

                # check bottom
                if not has_adjacent_part and i < len(schematic_lines) - 1:
                    has_adjacent_part = is_part_cell(schematic_lines[i + 1][j])
                    #print(c, 'bottom', has_adjacent_part)

                num_buffer += c

            # number ended -> commit
            elif len(num_buffer) > 0:
                # last number -> check right
                if not has_adjacent_part and j < len(schematic_lines[i]):
                    has_adjacent_part = has_parts_end(schematic_lines, i, j)
                    #print(line[j - 1], 'right', has_adjacent_part)

                # part_numbers.append((int(num_buffer), has_adjacent_part))
                if has_adjacent_part:
                    part_numbers.append(int(num_buffer))
                num_buffer = ''
                has_adjacent_part = False

        # line and number ended -> commit
        if len(num_buffer) > 0:
            if has_adjacent_part:
                part_numbers.append(int(num_buffer))

    return part_numbers

with open('input.txt', 'r', encoding='ascii') as f:
    input_lines = [l.strip() for l in f.readlines()]

part_numbers = task(input_lines)

print( sum(part_numbers) )
