input = __import__('sys').stdin.readline

mod = 1000000009

def init():
    dp = [0 for _ in range(1000000 + 1)]
    dp[1] = 1
    dp[2] = 2
    dp[3] = 4
    def f(x):
        if x == 1 or x == 2 or x == 3:
            return
        dp[x] = (dp[x-1] + dp[x-2] + dp[x-3]) % mod

    for i in range(1, 1000000 + 1):
        f(i)
    return dp

res = init()
def solution():
    n = int(input())
    print(res[n])

for _ in range(int(input())):
    solution()