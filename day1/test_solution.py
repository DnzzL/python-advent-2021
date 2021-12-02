from solution import part_one, part_two

with open("day1/test.txt", "r") as f:
    data_one = [int(line.strip()) for line in f]


def test_part_one():
    assert part_one(data_one) == 7


def test_part_two():
    assert part_two(data_one) == 5
