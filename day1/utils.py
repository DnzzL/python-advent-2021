def read_data(fname):
    with open(fname, "r") as f:
        data = [int(line.strip()) for line in f]
    return data
