# Naive solution not Scalable with exponential growth
# def part_one(data: dict, ran=80) -> int:
#     for i in range(ran):
#         zero_count = np.count_nonzero(data == 0)
#         data = np.where(data != 0, data - 1, 6)
#         if zero_count:
#             data = np.append(data, [8 for _ in range(zero_count)])
#     return len(data)


def part_one(data: dict, ran=80) -> int:
    lifespans = {i: 0 for i in range(8)}
    for d in data:
        lifespans[d] += 1
    for day in range(ran):
        lifespans = {
            d: (0 if lifespans.get(d + 1) is None else lifespans.get(d + 1))
            for d in range(-1, 8)
        }
        if lifespans.get(-1):
            lifespans[8] = lifespans[-1]
            lifespans[6] += lifespans[-1]
            lifespans[-1] = 0
    return sum(lifespans.values())


def part_two(data: dict) -> int:
    return part_one(data, 256)


if __name__ == "__main__":
    data = []
    with open("./input_one.txt", "r") as f:
        data = [int(i) for i in next(f).split(",")]
    print(part_one(data))
    print(part_two(data))
