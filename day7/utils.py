import numpy as np


def read_data(fname):
    data = []
    with open(fname, "r") as f:
        data = np.array([int(i) for i in next(f).split(",")])
    return data
