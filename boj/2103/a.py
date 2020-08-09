input = __import__('sys').stdin.readline

def solution():
    n = int(input())
    dic_x = {}
    dic_y = {}

    for i in range(n):
        xi, yi = map(int, input().split())
        if yi in dic_x:
            dic_x[yi].append(xi)
        else:
            dic_x[yi] = [xi]

        if xi in dic_y:
            dic_y[xi].append(yi)
        else:
            dic_y[xi] = [yi]

    group_x = []
    group_y = []
    for _, vx in dic_x.items():
        vx.sort()
        for i, _ in enumerate(vx):
            if i % 2 == 0:
                group_x.append((vx[i], vx[i + 1]))

    for _, vy in dic_y.items():
        vy.sort()
        for j, _ in enumerate(vy):
            if j % 2 == 0:
                group_y.append((vy[j], vy[j + 1]))

    ans = 0
    for xa in group_x:
        ans += xa[1] - xa[0]

    for yb in group_y:
        ans += yb[1] - yb[0]

    print(ans)

solution()