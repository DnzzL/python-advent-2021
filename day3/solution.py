from collections import Counter


def part_one(data: list) -> int:
    """Each bit in the gamma rate can be determined by finding the most common bit in the corresponding position
    of all numbers in the diagnostic report.
    The epsilon rate is calculated in a similar way; rather than use the most common bit,
    the least common bit from each position is used.

    Args:
        data (list): [input data]

    Returns:
        int: [result]
    """
    n = len(data[0])
    gamma = ""
    epsilon = ""
    for i in range(n):
        cnt = Counter(list(map(lambda x: x[i], data))).most_common(2)
        gamma += cnt[0][0]
        epsilon += cnt[1][0]
    return int(gamma, 2) * int(epsilon, 2)


def part_two(data: list) -> int:
    """To find oxygen generator rating, determine the most common value (0 or 1) in the current bit position,
    and keep only numbers with that bit in that position. If 0 and 1 are equally common,
    keep values with a 1 in the position being considered.
    To find CO2 scrubber rating, determine the least common value (0 or 1) in the current bit position,
    and keep only numbers with that bit in that position. If 0 and 1 are equally common,
    keep values with a 0 in the position being considered.

        Args:
            data (list): [input data]

        Returns:
            int: [result]
    """
    oxygen = data
    i = 0
    while len(oxygen) > 1:
        oxygen_candidates = set([i for i in range(len(oxygen))])
        i_bits = list(map(lambda x: x[i], oxygen))
        cnt = Counter(i_bits).most_common(2)
        most_common_count = cnt[0][1]
        most_common_bit = cnt[0][0] if most_common_count > len(oxygen) / 2 else "1"
        oxygen_candidates = set(
            [i for i, b in enumerate(i_bits) if b == most_common_bit]
        )
        oxygen = [oxygen[idx] for idx in list(oxygen_candidates)]
        i += 1

    co2 = data
    j = 0
    while len(co2) > 1:
        co2_candidates = set([i for i in range(len(co2))])
        i_bits = list(map(lambda x: x[j], co2))
        cnt = Counter(i_bits).most_common(2)
        least_common_bit = cnt[1][1]
        least_common_bit = cnt[1][0] if least_common_bit < len(co2) / 2 else "0"
        co2_candidates = set([i for i, b in enumerate(i_bits) if b == least_common_bit])
        co2 = [co2[idx] for idx in list(co2_candidates)]
        j += 1

    return int(oxygen[0], 2) * int(co2[0], 2)


if __name__ == "__main__":
    with open("./input_one.txt", "r") as f:
        data = [line.strip() for line in f]
    print(part_one(data))
    print(part_two(data))
