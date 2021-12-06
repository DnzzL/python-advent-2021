from solution import part_one, part_two
import numpy as np

with open("./test_one.txt", "r") as f:
    draws = next(f).strip().split(",")
    data = [line.strip().replace("  ", " ").split(" ") for line in f if len(line) > 1]
grids = {}
for i in range(0, len(data), 5):
    grids[i] = np.array(data[i : i + 5]).reshape(5, 5).astype(int)


# def test_part_one():
#     assert part_one(draws, grids) == 4512


def test_part_two():
    assert part_two(draws, grids) == 1924
