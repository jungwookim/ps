input = __import__('sys').stdin.readline
from collections import deque

def solution():
    q = deque()
    m, n, k = map(int, input().split())
    to_visit = [[False for _ in range(n)] for _ in range(m)]
    def bfs(x, y):
        if x >= m or y >= n or x <= -1 or y <= -1:
            return
        if not to_visit[x][y]:
            return
        to_visit[x][y] = False

        q.append((x+1, y))
        q.append((x-1, y))
        q.append((x, y+1))
        q.append((x, y-1))

    for _ in range(k):
        a, b = map(int, input().split())
        to_visit[a][b] = True
    
    cnt = 0
    for i in range(m):
        for j in range(n):
            if to_visit[i][j] == True:
                q.append((i, j))
                while len(q) != 0:
                    _x, _y = q.popleft()
                    bfs(_x, _y)
                cnt += 1
    print(cnt)

for _ in range(int(input())):
    solution()
