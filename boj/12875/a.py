input = __import__('sys').stdin.readline
from collections import deque

def solution():
    n = int(input())
    d = int(input())

    parents = [[] for _ in range(n)]
    for i in range(n):
        a = list(input().strip())
        for j in range(n):
            if a[j] == 'Y':
                parents[i].append(j)

    
    q = deque()
    def bfs(x):
        visited = [False for _ in range(n)]
        distance = [float('inf') for _ in range(n)]
        visited[x] = True
        q.append((x, 0))
        while q:
            a, b = q.popleft()
            distance[a] = b
            b += 1
            for p in parents[a]:
                if not visited[p]:
                    visited[p] = True
                    q.append((p, b))

        return distance
        
    maxv = 0
    for i in range(n):
        distance = bfs(i)
        maxd = max(distance)
        if maxv < maxd:
            maxv = maxd
    if maxv == float('inf'):
        print(-1)
    else:
        print(d*maxv)
        

solution()