input = __import__('sys').stdin.readline

def solution():
    n = int(input())

    a = [list(map(int, input().split())) for _ in range(n)]

    dp = [[0, 0, 0] for _ in range(n)]

    def f(x, c):
        if x == 0:
            dp[x][c] = a[0][c]
            return

        dp[x][c] = a[x][c] + min([ai for i, ai in enumerate(dp[x-1]) if i != c])

    for i in range(n):
        for j in range(3):
            f(i, j)

    print(min(dp[-1]))
solution()

