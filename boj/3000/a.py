input = __import__('sys').stdin.readline

def solution():
    n = int(input())
    points = [list(map(int, input().split())) for _ in range(n)]
    x_list = [0 for _ in range(100001)]
    y_list = [0 for _ in range(100001)]

    for p in points:
        [x, y] = p
        x_list[y] += 1
        y_list[x] += 1

    ans = 0
    for p in points:
        [x, y] = p
        add = (x_list[y] - 1) * (y_list[x] - 1)
        ans += add if add > 0 else 0

    print(ans)

solution()