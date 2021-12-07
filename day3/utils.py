def read_data(fname):
    with open(fname, "r") as f:
        data = [line.strip() for line in f]
    return data
