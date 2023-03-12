input = __import__('sys').stdin.readline
from collections import deque

n, m = map(int, input().split())
matrix = []
visited = [[False for _ in range(m)] for _ in range(n)]

for i in range(n):
    a = list(input())[:-1]
    a = list(map(int, a))
    matrix.append(a)

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

queue = deque()

def bfs(i, j):
    queue.append((i, j))
    visited[i][j] = True
    while queue:
        x, y = queue.popleft()
        for k in range(4):
            next_x = x + dx[k]
            next_y = y + dy[k]
            # 좌표 유효성 확인 후 맵 확인
            if next_x >= 0 and next_y >= 0 and next_x < n and next_y < m and visited[next_x][next_y] == False and matrix[next_x][next_y] != 0:
                visited[next_x][next_y] = True
                matrix[next_x][next_y] = matrix[x][y] + 1
                queue.append((next_x, next_y))

bfs(0, 0)
print(matrix[n-1][m-1])
