input = __import__('sys').stdin.readline

def solution():
    n = int(input())
    a = list(map(int, input().split()))

    dp = [[0 for _ in range(n + 5)] for _ in range(n + 5)]

    def f(a): # l <= r
        if l == 1 and r == 1:
            dp[1][1] = a[0]
        print('i, j', i, j)
        dp[l][r] = max(dp[l-1][r] + a[l-1], dp[l][r-1] + a[r-1])

    for i in range(1, n+1):
        for j in range(i, n+1):
            f(i, j)

    print(dp)
    ans = float("-inf")
    for e in dp:
        for ei in e:
            if ei > ans:
                ans = ei
    print(ans)

solution()