def read_data(fname):
    with open(fname, "r") as f:
        draws = next(f).strip().split(",")
        data = [
            line.strip().replace("  ", " ").split(" ") for line in f if len(line) > 1
        ]
    grids = {}
    for i in range(0, len(data), 5):
        grids[i] = np.array(data[i : i + 5]).reshape(5, 5).astype(int)
    return draws, grids
