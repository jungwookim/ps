input = __import__('sys').stdin.readline

def solution():
    n = int(input())
    p = [0] + list(map(int, input().split()))

    dp = [0 for _ in range(n+1)]

    def f(x):
        if x == 1:
            dp[1] == p[1]

        dp[x] = max([dp[x - i] + p[i] for i in range(1, x + 1)])

    for i in range(1, n+1):
        f(i)
    return dp[n]

print(solution())