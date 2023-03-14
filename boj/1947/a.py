input = __import__('sys').stdin.readline

def solution():
    n = int(input())
    dp = [0 for _ in range(1000000+1)]
    mod = 1000000000
    dp[1] = 0
    dp[2] = 1
    for i in range(3, n+1):
        dp[i] = (i-1) * (dp[i-1] + dp[i-2]) % mod # dp[i-2] : swap case dp, dp[i-1] : no swap case

    print(dp[n])
    
solution()

