input = __import__('sys').stdin.readline

def solution():
    n = int(input())
    dp = [[0 for _ in range(10)] for _ in range(n+1)] # 길이가 n일 때 높이 H로 끝나는 계단 수의 경우의 수
    mod = 1000000000

    for i in range(1, 10):
        dp[1][i] = 1

    for i in range(2, n+1):
        dp[i][0] = dp[i-1][1]
        dp[i][9] = dp[i-1][8]
        for j in range(1, 9):
            dp[i][j] = (dp[i-1][j-1] + dp[i-1][j+1]) % mod

    ans = 0

    for i in range(10):
        ans = (ans + dp[n][i]) % mod

    print(ans)

solution()
