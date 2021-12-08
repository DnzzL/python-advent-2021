import numpy as np

from utils import read_data


def part_one(signals: list, outputs: list) -> int:
    """Because the digits 1, 4, 7, and 8 each use a unique number of segments,
    you should be able to tell which combinations of signals correspond to those digits.
    In the output values, how many times do digits 1, 4, 7, or 8 appear?

    Args:
        signals (list): [input]
        outputs (list): [input]

    Returns:
        int: [result]
    """
    instances = 0
    unique_lengths = [2, 4, 3, 7]
    for o in outputs:
        instances += len(list(filter(lambda x: len(x) in unique_lengths, o)))
    return instances


def part_two(signals: list, outputs: list) -> int:
    """For each entry, determine all of the wire/segment connections and decode the four-digit output values.
    What do you get if you add up all of the output values?

    Args:
        signals (dict): [data]
        outputs (dict): [data]

    Returns:
        int: [result]
    """
    mapping = {
        "abcefg": 0,
        "cf": 1,
        "acdeg": 2,
        "acdfg": 3,
        "bcdf": 4,
        "abdfg": 5,
        "abdefg": 6,
        "acf": 7,
        "abcdefg": 8,
        "abcdfg": 9,
    }


if __name__ == "__main__":
    signals, outputs = read_data("./input.txt")

    print(part_one(signals, outputs))
