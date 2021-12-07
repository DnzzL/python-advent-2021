from solution import part_one, part_two
from utils import read_data

data = read_data("test.txt")


def test_part_one():
    assert part_one(data) == 37


def test_part_two():
    assert part_two(data) == 168
