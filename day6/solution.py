from utils import read_data

# Naive solution not Scalable with exponential growth
# def part_one(data: dict, ran=80) -> int:
#     for i in range(ran):
#         zero_count = np.count_nonzero(data == 0)
#         data = np.where(data != 0, data - 1, 6)
#         if zero_count:
#             data = np.append(data, [8 for _ in range(zero_count)])
#     return len(data)


def part_one(data: list, ran=80) -> int:
    """Each lanternfish creates a new lanternfish once every 7 days.
    Each day, a 0 becomes a 6 and adds a new 8 to the end of the list,
    while each other number decreases by 1 if it was present at the start of the day.
    How many lanternfish would there be after 80 days?

    Args:
        data (list): [input]
        ran (int, optional): [number of days]. Defaults to 80.

    Returns:
        int: [result]
    """
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


def part_two(data: list) -> int:
    """How many lanternfish would there be after 256 days?

    Args:
        data (list): [data]

    Returns:
        int: [result]
    """
    return part_one(data, 256)


if __name__ == "__main__":
    data = read_data("./input.txt")

    print(part_one(data))
    print(part_two(data))
