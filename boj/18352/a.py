input = __import__('sys').stdin.readline
from collections import deque
def solution():
    n, m, k, x = map(int, input().split())

    a = [[] for _ in range(n+1)]

    for _ in range(m):
        s, d = map(int, input().split())
        a[s].append(d)

    
    ans = [0 for _ in range(n+1)]
    visited = [False for _ in range(n+1)]
    q = deque()
    q.append([x, 0])

    while q:
        v, cnt = q.popleft()
        if not visited[v]:
            visited[v] = True
            ans[v] = cnt
            for vi in a[v]:
                q.append([vi, cnt + 1])
    result = []
    for i, v in enumerate(ans):
        if v == k:
            result.append(i)

    if len(result) == 0:
        print(-1)
    else:
        for r in result:
            print(r)

solution()