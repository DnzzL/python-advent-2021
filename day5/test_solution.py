from solution import part_one, part_two
import numpy as np

data = []
with open("./test_one.txt", "r") as f:
    for line in f:
        coords = line.strip().split(" -> ")
        data.append(coords[0].split(","))
        data.append(coords[1].split(","))
data = np.array(data).astype(int)


def test_part_one():
    assert part_one(data) == 5


def test_part_two():
    assert part_two(data) == 12
