input = __import__('sys').stdin.readline
from collections import deque

def solution():
    n, m, v = map(int, input().split())

    edge = ([[] for _ in range(n+1)])
    for _ in range(m):
        a, b = map(int, input().split())
        edge[a].append(b)
        edge[b].append(a)

    for e in edge:
        e.sort()

    dfs_result = []
    dfs_visited = [False for _ in range(n+1)]

    def dfs(x):
        if dfs_visited[x]:
            return
        dfs_result.append(x)
        dfs_visited[x] = True

        for node in edge[x]:
            dfs(node)

    dfs(v)
    print(*dfs_result)

    q = deque([])
    bfs_result = []
    bfs_visited = [False for _ in range(n+1)]

    def bfs(x):
        bfs_visited[x] = True
        q.append(x)

        while q:
            node = q.popleft()
            bfs_result.append(node)
            for c in edge[node]:
                if bfs_visited[c]:
                    continue
                bfs_visited[c] = True
                q.append(c)

    bfs(v)
    print(*bfs_result)      

solution()
