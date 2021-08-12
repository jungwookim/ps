input = __import__('sys').stdin.readline
from collections import deque
def solution():
    n = int(input())
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())

    q = deque()
    def bfs(x, y, cnt):
        nonlocal x2
        nonlocal y2
        
        q.append((x, y, cnt))

        visited = [[False for _ in range(n)] for _ in range(n)]
        while q:
            a, b, c = q.popleft()
            if a == x2 and b == y2:
                print(c)
                return
            visited[a][b] = True
            
            for i, j in [(2, 1), (1, 2), (-2, -1), (-1, -2), (2, -1), (1, -2), (-2, 1), (-1, 2)]:
                if a+i < 0 or b+j < 0 or a+i >= n or b+j >= n:
                    continue
                if visited[a+i][b+j]:
                    continue
                visited[a+i][b+j] = True

                q.append((a+i, b+j, c+1))

    bfs(x1, y1, 0)
for _ in range(int(input())):
    solution()