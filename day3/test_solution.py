from solution import part_one, part_two

with open("./test_one.txt", "r") as f:
    data_one = [line.strip() for line in f]


def test_part_one():
    assert part_one(data_one) == 198


def test_part_two():
    assert part_two(data_one) == 230