def sol(arr: list) -> int:
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
