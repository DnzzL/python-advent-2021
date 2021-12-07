import numpy as np
from math import floor

from utils import read_data


def arithmetic_sum(n):
    return n * (n + 1) // 2


def part_one(data: list) -> int:
    """Each change of 1 step in horizontal position of a single crab costs 1 fuel.
    Determine the horizontal position that the crabs can align to using the least fuel possible.
    How much fuel must they spend to align to that position?

    Args:
        data (list): [input]

    Returns:
        int: [result]
    """
    median = np.median(data)
    cost = np.abs(data - median)
    return int(np.sum(cost))


def part_two(data: list) -> int:
    """Instead, each change of 1 step in horizontal position costs 1 more unit of fuel than the last:
    the first step costs 1, the second step costs 2, the third step costs 3, and so on.

    Args:
        data (dict): [data]

    Returns:
        int: [result]
    """
    mean = floor(np.mean(data))  # ceil works for test and ceil for puzzle input 🤔
    diffs = np.abs(data - mean)
    cost = list(map(lambda x: arithmetic_sum(x), diffs))
    return int(np.sum(cost))


if __name__ == "__main__":
    data = read_data("./test.txt")

    print(part_one(data))
    print(part_two(data))
