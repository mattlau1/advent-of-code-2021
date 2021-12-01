def sol(arr: list) -> int:
    sums = []
    for i in range(len(arr) - 2):
        m_one = arr[i]
        m_two = arr[i + 1]
        m_three = arr[i + 2]
        sums.append(m_one + m_two + m_three)
    return sol1(sums)


def sol1(arr: list) -> int:
    count = 0
    for i in range(1, len(arr)):
        prev = arr[i - 1]
        curr = arr[i]
        if curr > prev:
            count += 1
    return count


if __name__ == "__main__":
    arr = []
    with open("input.txt") as f:
        lines = f.readlines()
        for line in lines:
            arr.append(int(line))
    print(sol(arr))
