def part_one(data: list) -> int:
    nb_increase = 0
    for i, j in zip(data, data[1:]):
        if j > i:
            nb_increase += 1
    return nb_increase


def part_two(data: list) -> int:
    nb_increase = 0
    previous_sum = None
    for i, j, k in zip(data, data[1:], data[2:]):
        current_sum = i + j + k
        if previous_sum and current_sum > previous_sum:
            nb_increase += 1
        previous_sum = current_sum
    return nb_increase


if __name__ == "__main__":
    with open("day1/input_one.txt", "r") as f:
        data = [int(line.strip()) for line in f]
    result = part_one(data)
    print(result)

    result = part_two(data)
    print(result)
