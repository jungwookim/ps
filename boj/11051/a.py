input = __import__('sys').stdin.readline

def solution():
    n, k = map(int, input().split())
    dp = [[0 for _ in range(n+1)] for _ in range(n+1)]

    mod = 10007
    for i in range(1, n+1):
        dp[i][1] = i % mod
        dp[i][0] = 1 % mod
        dp[i][i] = 1 % mod

    for i in range(2, n+1):
        for j in range(1, i):
            dp[i][j] = (dp[i-1][j] + dp[i-1][j-1]) % mod
    print(dp[n][k])

solution()