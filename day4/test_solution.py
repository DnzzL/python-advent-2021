from solution import part_one, part_two
import numpy as np
from copy import deepcopy

from utils import read_data

data = read_data("test.txt")


def test_part_one():
    assert part_one(draws, deepcopy(grids)) == 4512


def test_part_two():
    assert part_two(draws, deepcopy(grids)) == 1924
