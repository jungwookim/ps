input = __import__('sys').stdin.readline
import sys
sys.setrecursionlimit(10**6)

def solution():
    m, n, k = map(int, input().split())
    to_visit = [[False for _ in range(n)] for _ in range(m)]
    def dfs(x, y):
        if x >= m or y >= n or x <= -1 or y <= -1:
            return
        if not to_visit[x][y]:
            return
        to_visit[x][y] = False

        dfs(x + 1, y)
        dfs(x - 1, y)
        dfs(x, y + 1)
        dfs(x, y - 1)

    for _ in range(k):
        a, b = map(int, input().split())
        to_visit[a][b] = True
    
    cnt = 0
    for i in range(m):
        for j in range(n):
            if to_visit[i][j] == True:
                dfs(i, j)
                cnt += 1
    print(cnt)

for _ in range(int(input())):
    solution()
