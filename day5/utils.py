def read_data(fname):
    data = []
    with open(fname, "r") as f:
        for line in f:
            coords = line.strip().split(" -> ")
            data.append(coords[0].split(","))
            data.append(coords[1].split(","))
    data = np.array(data).astype(int)
    return data
