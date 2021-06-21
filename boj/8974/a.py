def solution():
    a, b = map(int, input().split())

    i = 0
    l = []
    for _ in range(1001):
        for _ in range(i):
            if len(l) == 1000:
                break
            l.append(i)
        i += 1

        if len(l) == 1000:
            break
    print(sum(l[a - 1:b]))

solution()