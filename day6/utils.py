def read_data(fname):
    data = []
    with open(fname, "r") as f:
        data = [int(i) for i in next(f).split(",")]
    return data
