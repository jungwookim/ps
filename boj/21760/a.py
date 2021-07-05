input = __import__('sys').stdin.readline

def solution():
    n, m, k, d = map(int, input().split())

    b = 1
    ans = -1

    while True:
        # in the same league
        x = m * (m - 1) * n * k * b // 2

        # other league
        y = m ** n * b

        if x + y <= d:
            b += 1
            ans = x + y
            continue
        else:
            print(ans)
            break

for _ in range(int(input())):
    solution()
