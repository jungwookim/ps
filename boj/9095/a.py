input = __import__('sys').stdin.readline

def solution():
    n = int(input())

    if n == 1:
        print(1)
        return
    if n == 2:
        print(2)
        return
    if n == 3:
        print(4)
        return

    dp = [0 for _ in range(n + 1)]
    dp[1] = 1
    dp[2] = 2
    dp[3] = 4
    def f(x):
        if x == 1 or x == 2 or x == 3:
            return
        dp[x] = dp[x-1] + dp[x-2] + dp[x-3]

    for i in range(1, n + 1):
        f(i)

    print(dp[n])
for _ in range(int(input())):
    solution()