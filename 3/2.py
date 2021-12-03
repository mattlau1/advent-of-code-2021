def oxygen_generator_rating(arr: list, bit: int):
    if len(arr) == 1 or bit == len(arr[0]):
        return str(arr[0])

    zero_count = 0
    one_count = 0
    zero_nums = []
    one_nums = []
    for num in arr:
        if num[bit] == '0':
            zero_count += 1
            zero_nums.append(num)
        else:
            one_count += 1
            one_nums.append(num)

    most_common = '0' if max(zero_count, one_count) == zero_count else '1'
    if zero_count == one_count:
        return oxygen_generator_rating(one_nums, bit + 1)
    elif most_common == '0':
        # keep all numbres with bit number 'bit' == '0'
        return oxygen_generator_rating(zero_nums, bit + 1)
    else:
        return oxygen_generator_rating(one_nums, bit + 1)


def co2_scrubber_rating(arr: list, bit: int):
    if len(arr) == 1 or bit == len(arr[0]):
        return str(arr[0])

    zero_count = 0
    one_count = 0
    zero_nums = []
    one_nums = []
    for num in arr:
        if num[bit] == '0':
            zero_count += 1
            zero_nums.append(num)
        else:
            one_count += 1
            one_nums.append(num)

    most_common = '0' if max(zero_count, one_count) == zero_count else '1'
    if zero_count == one_count:
        return co2_scrubber_rating(zero_nums, bit + 1)
    elif most_common == '0':
        # keep all numbres with bit number 'bit' == '1'
        return co2_scrubber_rating(one_nums, bit + 1)
    else:
        return co2_scrubber_rating(zero_nums, bit + 1)


def sol(arr: list):
    return int(oxygen_generator_rating(arr, 0), 2) * int(co2_scrubber_rating(arr, 0), 2)


if __name__ == "__main__":
    arr = []
    with open("input.txt") as f:
        lines = f.readlines()
        for line in lines:
            arr.append(line.rstrip())
    print(sol(arr))
