import numpy as np


def is_horizontal_line(start: tuple, end: tuple):
    (_, y1) = start
    (_, y2) = end
    return y1 == y2


def is_vertical_line(start: tuple, end: tuple):
    (x1, _) = start
    (x2, _) = end
    return x1 == x2


def get_horizontal_line(start: tuple, end: tuple) -> list:
    (x1, y1) = start
    (x2, _) = end
    if x2 > x1:
        return [(i, y1) for i in range(x1, x2 + 1)]
    return [(i, y1) for i in range(x2, x1 + 1)]


def get_vertical_line(start: tuple, end: tuple) -> list:
    (x1, y1) = start
    (_, y2) = end
    if y2 > y1:
        return [(x1, j) for j in range(y1, y2 + 1)]
    return [(x1, j) for j in range(y2, y1 + 1, 1)]


def get_diagonal_line(start: tuple, end: tuple) -> list:
    (x1, y1) = start
    (x2, y2) = end
    xs = range(x1, x2 + 1) if x1 < x2 else range(x1, x2 - 1, -1)
    ys = range(y1, y2 + 1) if y1 < y2 else range(y1, y2 - 1, -1)
    return [(i, j) for i, j in zip(xs, ys)]


def part_one(data: dict) -> int:
    """To avoid the most dangerous areas, you need to determine the number of points where at least two lines overlap.
    For now, only consider horizontal and vertical lines: lines where either x1 = x2 or y1 = y2.

    Args:
        data (dict): [input]

    Returns:
        int: [result]
    """
    max_value = np.max(data.flatten()) + 1
    overlaps = np.zeros((max_value, max_value)).astype(int)
    for (start, end) in zip(data[0::2], data[1::2]):
        if is_horizontal_line(start, end):
            line = get_horizontal_line(start, end)
        elif is_vertical_line(start, end):
            line = get_vertical_line(start, end)
        else:
            continue
        for (x, y) in line:
            overlaps[y][x] += 1
    return (overlaps.flatten() > 1).sum()


def part_two(data: dict) -> int:
    """Unfortunately, considering only horizontal and vertical lines doesn't give you the full picture;
    you need to also consider diagonal lines.
    You still need to determine the number of points where at least two lines overlap.

    Args:
        data (dict): [input]

    Returns:
        int: [result]
    """
    max_value = np.max(data.flatten()) + 1
    overlaps = np.zeros((max_value, max_value)).astype(int)
    for (start, end) in zip(data[0::2], data[1::2]):
        if is_horizontal_line(start, end):
            line = get_horizontal_line(start, end)
        elif is_vertical_line(start, end):
            line = get_vertical_line(start, end)
        else:
            line = get_diagonal_line(start, end)
        for (x, y) in line:
            overlaps[y][x] += 1
    return (overlaps.flatten() > 1).sum()


if __name__ == "__main__":
    data = []
    with open("./input_one.txt", "r") as f:
        for line in f:
            coords = line.strip().split(" -> ")
            data.append(coords[0].split(","))
            data.append(coords[1].split(","))
    data = np.array(data).astype(int)

    print(part_one(data))
    print(part_two(data))
