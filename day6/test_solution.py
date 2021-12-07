from solution import part_one, part_two

data = []
with open("./input_one.txt", "r") as f:
    data = [int(i) for i in next(f).split(",")]


def test_part_one():
    assert part_one(data) == 5934


def test_part_two():
    assert part_two(data) == 386536
