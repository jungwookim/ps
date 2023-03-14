input = __import__('sys').stdin.readline

def solution():
    n, m, k = map(int, input().split())
    dp = [[1 for _ in range(m+1)] for _ in range(n+1)] # dp stores the number of combinations with i, j

    for i in range(1, n+1):
        for j in range(1, m+1):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]

    if dp[n][m] < k:
        print(-1)
        return
    ans = ""
    while 1:
        if n == 0:
            ans += ("z" * m)
            break
        if m == 0:
            ans += ("a" * n)
            break
        v = dp[n-1][m] # a로 시작할 때 갯수
        if v >= k:
            ans += "a"
            n -= 1
        else:
            ans += "z"
            m -= 1
            k -= v
    print(ans)

solution()
