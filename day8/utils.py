import numpy as np


def read_data(fname):
    data = []
    with open(fname, "r") as f:
        signals = []
        outputs = []
        for line in f:
            signal, output = line.strip().split(" | ")
            signals.append(signal.split(" "))
            outputs.append(output.split(" "))
    return signals, outputs
