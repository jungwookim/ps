mod = 10007

def solution():
    n = int(input())

    dp = [0 for _ in range(n + 1)]

    def f(x):
        if x == 1:
            dp[x] == 1
            return
        if x == 2:
            dp[x] = 2
            return
        if x == 3:
            dp[x] = 3
            return
        dp[x] = dp[x-1] * 2 + dp[x-1] * 3
    for i in range(1, n + 1):
        f(i)

    print(dp[n])

solution()