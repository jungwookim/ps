input = __import__('sys').stdin.readline


def solution():
    k = int(input())
    base = [[0, 0] for _ in range(6)]
    x_list = []
    y_list = []
    for i in range(6):
        if i == 5:
            break
        x, y = map(int, input().split())
        if x == 1:
            base[i + 1][0] = base[i][0] + y
            base[i + 1][1] = base[i][1]
        elif x == 2:
            base[i + 1][0] = base[i][0] - y
            base[i + 1][1] = base[i][1]
        elif x == 3:
            base[i + 1][1] = base[i][1] - y
            base[i + 1][0] = base[i][0]
        elif x == 4:
            base[i + 1][1] = base[i][1] + y
            base[i + 1][0] = base[i][0]

    for b in base:
        if b[0] not in x_list:
            x_list.append(b[0])
        if b[1] not in y_list:
            y_list.append(b[1])

    x_list.sort()
    y_list.sort()

    four_points = [[x_list[0], y_list[0]], [x_list[0], y_list[-1]], [
        x_list[-1], y_list[0]], [x_list[-1], y_list[-1]]]

    big = abs(x_list[0] - x_list[-1]) * abs(y_list[0] - y_list[-1])
    small = 0
    inner_point = [x_list[1], y_list[1]]
    for p in four_points:
        find = False
        for b in base:
            if p[0] == b[0] and p[1] == b[1]:
                find = True
        if not find:
            small = abs(p[0] - inner_point[0]) * abs(p[1] - inner_point[1])

    print((big - small) * k)


solution()
