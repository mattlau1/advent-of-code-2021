def sol(arr: list) -> int:
    directions = ['forward', 'down', 'up']
    horizontal = 0
    depth = 0
    for i in arr:
        dir = i.split(' ')[0]
        units = i.split(' ')[1]
        if dir == directions[0]:
            horizontal += int(units)
        elif dir == directions[1]:
            depth += int(units)
        elif dir == directions[2]:
            depth -= int(units)
    print(horizontal)
    print(depth)
    return horizontal * depth


if __name__ == "__main__":
    arr = []
    with open("input.txt") as f:
        lines = f.readlines()
        for line in lines:
            arr.append(line.rstrip())
    print(sol(arr))
