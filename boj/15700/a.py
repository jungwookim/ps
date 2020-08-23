def solution():
    n, m = map(int, input().split())

    qn = n // 2
    rn = n % 2

    qm = m // 2

    ans = 0
    ans += qn * m
    if rn == 1:
        ans += qm

    print(ans)

solution()