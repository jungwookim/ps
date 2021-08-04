input = __import__('sys').stdin.readline

def solution():
    n = int(input())
    a = [int(input()) for _ in range(n)]

    dp = [0 for _ in range(n + 1)]

    def f(x):
        if x == 1:
            dp[1] = a[0]
            return
        if x == 2:
            dp[2] = a[0] + a[1]
            return
        dp[x] = max(dp[x-2] + a[x-1], dp[x-1], dp[x-3] + a[x-2] + a[x-1])

    for i in range(1, n+1):
        f(i)

    print(max(dp))

solution()