input = __import__('sys').stdin.readline

def solution():
    n = int(input())

    dp = [[0, 0] for _ in range(n)] # [끝이 0인, 끝이 1인]

    def f(x):
        if x == 0:
            dp[x] = [0, 1]
            return
        dp[x] = [dp[x-1][1] + dp[x-1][0], dp[x-1][0]]

    for i in range(n):
        f(i)

    print(sum(dp[-1]))

solution()
