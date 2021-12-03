def sol(arr: list):
    gamma_rate = ''
    epsilon_rate = ''
    for bit in range(len(arr[0])):
        zero_count = 0
        one_count = 0
        for num in (arr):
            if num[bit] == '0':
                zero_count += 1
            else:
                one_count += 1

        most_common = max(zero_count, one_count)
        if most_common == zero_count:
            gamma_rate += '0'
            epsilon_rate += '1'
        else:
            gamma_rate += '1'
            epsilon_rate += '0'
    return int(gamma_rate, 2) * int(epsilon_rate, 2)


if __name__ == "__main__":
    arr = []
    with open("input.txt") as f:
        lines = f.readlines()
        for line in lines:
            arr.append(line.rstrip())
    print(sol(arr))
