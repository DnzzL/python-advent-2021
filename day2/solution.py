from utils import read_data


def part_one(data: list) -> int:
    """Calculate the horizontal position and depth you would have after following the planned course.
    What do you get if you multiply your final horizontal position by your final depth?

    Args:
        data (list): [input data]

    Returns:
        int: [result]
    """
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
    """In addition to horizontal position and depth, you'll also need to track a third value, aim, which also starts at 0.
    The commands also mean something entirely different than you first thought:

    down X increases your aim by X units.
    up X decreases your aim by X units.
    forward X does two things:
    It increases your horizontal position by X units.
    It increases your depth by your aim multiplied by X.

        Args:
            data (list): [input data]

        Returns:
            int: [result]
    """
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
    data = read_data("./input.txt")

    print(part_one(data))
    print(part_two(data))
