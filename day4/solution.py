import numpy as np


def has_horizontal_alignment(arr: np.array, played: list):
    for i in range(5):
        intersection = set(played).intersection(set(arr[i, :]))
        if len(intersection) == 5:
            return np.setdiff1d(arr, played).sum()
    return -1


def has_vertical_alignment(arr: np.array, played: list):
    for i in range(5):
        if len(set(played).intersection(set(arr[:, i]))) == 5:
            return np.setdiff1d(arr, played).sum()
    return -1


def part_one(draws: list, grids: dict) -> int:
    """
    Start by finding the sum of all unmarked numbers on that board; in this case, the sum is 188.
    Then, multiply that sum by the number that was just called when the board won, 24,
    to get the final score, 188 * 24 = 4512

    Args:
        draws (list): [draws]
        grids (dict): [bingo grids]

    Returns:
        int: [result]
    """
    played = []
    for i in range(len(draws)):
        played.append(int(draws.pop(0)))
        for grid in grids.values():
            horizontal = has_horizontal_alignment(grid, played)
            if horizontal != -1:
                return horizontal * played[-1]

            vertical = has_vertical_alignment(grid, played)
            if vertical != -1:
                return vertical * played[-1]


def part_two(draws: list, grids: dict) -> int:
    """In the above example, the second board is the last to win, which happens after 13 is eventually called
    and its middle column is completely marked. If you were to keep playing until this point,
    the second board would have a sum of unmarked numbers equal to 148 for a final score of 148 * 13 = 1924.

    Args:
        draws (list): [draws]
        grids (dict): [bingo grids]

    Returns:
        int: [result]
    """
    played = []
    wins = set()
    i = 0
    last_sum = 0
    for i in range(len(draws)):
        played.append(int(draws.pop(0)))
        for j, grid in list(grids.items()):
            horizontal = has_horizontal_alignment(grid, played)
            vertical = has_vertical_alignment(grid, played)
            if horizontal != -1:
                wins = wins.union(set([j]))
                i += 1
                last_sum = horizontal
                if len(wins) == len(grids):
                    return last_sum * played[-1]
            if vertical != -1:
                wins = wins.union(set([j]))
                i += 1
                last_sum = vertical
                if len(wins) == len(grids):
                    return last_sum * played[-1]


if __name__ == "__main__":
    with open("./input_one.txt", "r") as f:
        draws = next(f).strip().split(",")
        data = [
            line.strip().replace("  ", " ").split(" ") for line in f if len(line) > 1
        ]
    grids = {}
    for i in range(0, len(data), 5):
        grids[i] = np.array(data[i : i + 5]).reshape(5, 5).astype(int)

    # print(part_one(draws, grids))
    print(part_two(draws, grids))
