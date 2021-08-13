input = __import__('sys').stdin.readline
import sys

dp = [[[0 for _ in range(51)] for _ in range(51)] for _ in range(51)]
def w(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        dp[a][b][c] = 1
    elif a > 20 or b > 20 or c > 20:
        dp[a][b][c] = dp[20][20][20]
    elif a < b and b < c:
        dp[a][b][c] = dp[a][b][c-1] + dp[a][b-1][c-1] - dp[a][b-1][c]
    else:
        dp[a][b][c] = dp[a-1][b][c] + dp[a-1][b-1][c] + dp[a-1][b][c-1] - dp[a-1][b-1][c-1]

for i in range(51):
    for j in range(51):
        for k in range(51):
            w(i, j, k)

def solution():
    x, y, z = map(int, input().split())
    if x == -1 and y == -1 and z == -1:
        sys.exit()

    if x <= 0 or y <= 0 or z <= 0:
        print("w({}, {}, {}) = 1".format(x, y, z))
        return

    
    if x > 20 or y > 20 or z > 20:
        print("w({}, {}, {}) = {}".format(x, y, z, dp[20][20][20]))
    else:
        print("w({}, {}, {}) = {}".format(x, y, z, dp[x][y][z]))
while True:
    solution()