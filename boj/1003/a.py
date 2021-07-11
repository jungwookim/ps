input = __import__('sys').stdin.readline

def solution():
    n = int(input())
    dp = [[0, 0] for _ in range(n + 1)]
    def fib(x, d):
        if x == 0:
            if d == 0:
                dp[x][d] += 1
            return
        if x == 1:
            if d == 1:
                dp[x][d] += 1
            return
        for i in range(2):
            dp[x][i] = dp[x - 1][i] + dp[x - 2][i]
    
    for i in range(n + 1):
        for j in range(2):
            fib(i, j)
    print(*dp[n])

for _ in range(int(input())):
    solution()