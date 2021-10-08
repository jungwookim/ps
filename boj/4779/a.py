input = __import__('sys').stdin.readline
import sys

dp = ['-']

for i in range(1, 13):
    dp.append(dp[i-1] + ' ' * len(dp[i-1]) + dp[i-1])

def solution():
    n = input()
    if n == '':
        sys.exit()
    n = int(n)

    print(dp[n])

while 1:
    solution()