input = __import__('sys').stdin.readline
from collections import deque

def init(l):
    res = []
    for n, e in enumerate(l):
        if e == 0:
            res.append(n)
    return res

def solution():
    n, m = map(int, input().split())
    
    indegrees = [0 for _ in range(n)]
    edges = [[] for _ in range(n)]
    q = deque()
    for _ in range(m):
        a, b = map(int, input().split())
        indegrees[b-1] += 1
        edges[a-1].append(b-1)

    ans = []
    init_queue = init(indegrees)
    q += init_queue

    for _ in range(n):
        if len(q) == 0:
            return

        poped_v = q.popleft()
        ans.append(poped_v+1)
        for e in edges[poped_v]:
            indegrees[e] -= 1
            if indegrees[e] == 0:
                q.append(e)

    print(*ans)

solution()
        