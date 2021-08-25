input = __import__('sys').stdin.readline

def solution():
    n = int(input())

    dp = [0 for _ in range(32)]
    dp[0] = 1
    for x in range(1, 31):
        if x % 2 == 1:
            continue
        if x == 2:
            dp[x] = 3
            continue
        if x == 4:
            dp[x] = 11
            continue
        dp[x] = dp[x-2] * dp[2]
        for y in range(4, x+1, 2):
            dp[x] += dp[x-y] * 2
    print(dp[n])
solution()