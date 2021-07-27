input = __import__('sys').stdin.readline
from collections import deque

def solution():
    n, m = map(int, input().split())

    parents = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b = map(int, input().split())
        parents[b].append(a)

    q = deque([])
    result = [0 for _ in range(n+1)]
    def bfs(x):
        visited = [False for _ in range(n+1)]
        visited[x] = True
        result = 1
        q.append(x)
        while q:
            one = q.popleft()
            for p in parents[one]:
                if visited[p]:
                    continue
                visited[p] = True
                result += 1
                q.append(p)
        return result

    maxv = 0
    ans = []
    for i in range(1, n+1):
        res = bfs(i)
        if res > maxv:
            maxv = res
            ans = [i]
        elif res == maxv:
            ans.append(i)
            
    print(*ans)
solution()
