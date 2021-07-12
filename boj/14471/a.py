input = __import__('sys').stdin.readline

def solution():
    n, m = map(int, input().split())

    cost_candi = []
    valid = 0
    for _ in range(m):
        a, b = map(int, input().split())
        if a >= n:
            valid += 1
        else:
            cost_candi.append(n - a)

    if valid >= m - 1:
        print(0)
        return
    else:
        print(sum(sorted(cost_candi)[:m - 1 - valid]))
        return

solution()