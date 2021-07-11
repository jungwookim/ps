def solution():
    n = int(input())
    a = []
    for _ in range(n):
        a.append(list(map(int, input().split())))

    dp = [[0 for _ in range(i + 2)] for i in range(n + 1)]
    def f(x, i):
        if x == 1:
            dp[1][1] = a[0][0]
            return
        dp[x][i] = a[x-1][i-1] + max(dp[x-1][i-1], dp[x-1][i])


    for i in range(1, n + 1):
        for j in range(1, i + 1):
            f(i, j)

    print(max(dp[n]))

solution()