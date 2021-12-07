def read_data(fname):
    with open(fname, "r") as f:
        data = [line.strip().split(" ") for line in f]
    return data
