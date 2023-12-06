"""
--- Part Two ---

The Elf says they've stopped producing snow because they aren't getting any
water! He isn't sure why the water stopped; however, he can show you how to
get to the water source to check it out for yourself. It's just up ahead!

As you continue your walk, the Elf poses a second question: in each game
you played, what is the fewest number of cubes of each color that could
have been in the bag to make the game possible?

Again consider the example games from earlier:
    Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
    Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
    Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
    Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
    Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green

In game 1, the game could have been played with as few as 4 red, 2 green,
and 6 blue cubes. If any color had even one fewer cube, the game would
have been impossible.
    Game 2 could have been played with a minimum of 1 red, 3 green, and 4 blue cubes.
    Game 3 must have been played with at least 20 red, 13 green, and 6 blue cubes.
    Game 4 required at least 14 red, 3 green, and 15 blue cubes.
    Game 5 needed no fewer than 6 red, 3 green, and 2 blue cubes in the bag.
The power of a set of cubes is equal to the numbers of red, green, and blue
cubes multiplied together. The power of the minimum set of cubes in game 1 is 48.
In games 2-5 it was 12, 1560, 630, and 36, respectively. Adding up these five
powers produces the sum 2286.

For each game, find the minimum set of cubes that must have been present.
What is the sum of the power of these sets?
"""
COLORS = ['red', 'green', 'blue']

def task(game_results: dict[int, list[tuple[int, int, int]]]) -> list[int]:
    """ Solves the task.

    Args:
        :game_results   Dictionary of the games indexed by the game number, each
                        element containing a set of takes. A take is a list
                        containing the number of the cubes of each color.
                        A take is a 3-tuple, having the format: (red, green, blue).

    Returns:
        Dictionary of the minimum set of the games. The game
        number is used as an index, and the values are 3-tuples,
        which represent the minimum numbers of red, green and
        blue cubes, respectively.
    """
    minimum_sets = {}
    for game_number, game_result in game_results.items():
        minimum_set = [0, 0, 0]
        # go through the takes in the game
        for take in game_result:
            for i in [0, 1, 2]:
                # if there are more cubes of this color in this set, update the minimum set
                if take[i] > minimum_set[i]:
                    minimum_set[i] = take[i]

        minimum_sets[game_number] = tuple(minimum_set)

    return minimum_sets


with open('input.txt', 'r', encoding='ascii') as f:
   input_lines = [l.strip() for l in f.readlines()]

# parse the input lines to a game results list
game_results = {}
for line in input_lines:
    # extract the game number and the takes from the line
    game_number_str, game_result_str = line.split(': ')
    game_number = int(game_number_str[5:])

    # handle the takes in the game
    takes = []
    for take_str in game_result_str.split('; '):
        counts = [0, 0, 0]

        # handle the colors in the take
        for color_result_str in take_str.split(', '):
            num_cubes, color = color_result_str.split(' ')
            counts[COLORS.index(color)] += int(num_cubes)
        
        takes.append(tuple(counts))

    # store the results to the game result dictionary
    game_results[game_number] = takes

minimum_sets = task(game_results)
set_powers = [(r * g * b) for (r, g, b) in minimum_sets.values()]

print(f"Sum of set powers: {sum(set_powers)}")
