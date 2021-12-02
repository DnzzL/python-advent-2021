def part_one(data: list) -> int:
    horizontal_position = 0
    vertical_position = 0
    for instruction, units in data:
        if instruction == "up":
            vertical_position -= int(units)
        elif instruction == "down":
            vertical_position += int(units)
        else:
            horizontal_position += int(units)
    return horizontal_position * vertical_position


def part_two(data: list) -> int:
    horizontal_position = 0
    vertical_position = 0
    aim = 0
    for instruction, units in data:
        if instruction == "up":
            aim -= int(units)
        elif instruction == "down":
            aim += int(units)
        else:
            horizontal_position += int(units)
            vertical_position += aim * int(units)
    return horizontal_position * vertical_position


if __name__ == "__main__":
    with open("./input_one.txt", "r") as f:
        data = [line.strip().split(" ") for line in f]
    result = part_one(data)
    print(result)

    result = part_two(data)
    print(result)
