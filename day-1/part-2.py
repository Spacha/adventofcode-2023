"""
--- Part Two ---
Your calculation isn't quite right. It looks like some of the digits are
actually spelled out with letters: one, two, three, four, five, six, seven,
eight, and nine also count as valid "digits".

Equipped with this new information, you now need to find the real first and
last digit on each line. For example:
    two1nine
    eightwothree
    abcone2threexyz
    xtwone3four
    4nineeightseven2
    zoneight234
    7pqrstsixteen
In this example, the calibration values are 29, 83, 13, 24, 42, 14, and 76.
Adding these together produces 281.

What is the sum of all of the calibration values?
"""
from typing import Optional

VERBOSE = False

DIGITS = {'one':    '1',
          'two':    '2',
          'three':  '3',
          'four':   '4',
          'five':   '5',
          'six':    '6',
          'seven':  '7',
          'eight':  '8',
          'nine':   '9'}

def check_written_digit(buffer: str) -> Optional[str]:
    for digit, digit_numeric in DIGITS.items():
        if digit in buffer:
            return digit_numeric
    return None

def task(calibration_lines: list[str]) -> int:
    """ Solves the task.
        Takes the first and last numeric value from the line and concatenates them to a number.
    """
    calibration_values = []
    for line in calibration_lines:
        first_digit = None
        word_buffer = ''
        for c in line:
            # numeric -> break immediately
            if c.isnumeric():
                first_digit = c
                break

            # not numeric, keep buffering
            word_buffer += c
            first_digit = check_written_digit(word_buffer)
            if first_digit is not None:
                break

        last_digit = None
        word_buffer = ''
        for c in line[::-1]:
            # numeric -> break immediately
            if c.isnumeric():
                last_digit = c
                break

            # not numeric, keep buffering
            word_buffer = c + word_buffer
            last_digit = check_written_digit(word_buffer)
            if last_digit is not None:
                break

        if first_digit is None or last_digit is None:
            raise ValueError(f"Line '{line}' does not contain a numeric value.")

        calibration_values.append(int(first_digit + last_digit))
        if VERBOSE:
            print(f"{line:<30}{calibration_values[-1]}")

    return sum(calibration_values)

with open('input.txt', 'r', encoding='ascii') as f:
   input_lines = [l.strip() for l in f.readlines()]

print(f"\nSum of calibration values: {task(input_lines)}")
