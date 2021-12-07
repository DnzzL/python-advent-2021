from utils import read_data


def part_one(data: list) -> int:
    """count the number of times a depth measurement increases from the previous measurement

    Args:
        data (list): [input data]

    Returns:
        int: [result]
    """
    nb_increase = 0
    for i, j in zip(data, data[1:]):
        if j > i:
            nb_increase += 1
    return nb_increase


def part_two(data: list) -> int:
    """count the number of times the sum of measurements in this sliding window increases from the previous sum.
    So, compare A with B, then compare B with C, then C with D, and so on.
    Stop when there aren't enough measurements left to create a new three-measurement sum.

    Args:
        data (list): [input data]

    Returns:
        int: [result]
    """
    nb_increase = 0
    previous_sum = None
    for i, j, k in zip(data, data[1:], data[2:]):
        current_sum = i + j + k
        if previous_sum and current_sum > previous_sum:
            nb_increase += 1
        previous_sum = current_sum
    return nb_increase


if __name__ == "__main__":
    data = read_data("input.txt")

    print(part_one(data))
    print(part_two(data))
