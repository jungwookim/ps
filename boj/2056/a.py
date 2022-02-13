input = __import__('sys').stdin.readline
from collections import deque

def solution():
    n = int(input())
    indegrees = [0 for _ in range(n)]
    edges = [[] for _ in range(n)]
    results = []
    times = []
    for i in range(n):
        t, _, *s = map(int, input().split())
        if i == 0:
            times.append(t)
            results.append(t)
        if i != 0:
            times.append(t)
            results.append(t)
            pres = [si - 1 for si in s]
            for j in pres:
                edges[j].append(i)
            indegrees[i] = len(pres)

    q = deque()
    for i, indegree in enumerate(indegrees):
        if indegree == 0:
            q.append(i)

    ans = []
    while q:
        poped_v = q.popleft()
        ans.append(poped_v)
        for c in edges[poped_v]:
            indegrees[c] -= 1
            results[c] = max(results[c], results[poped_v] + times[c])
            if indegrees[c] == 0:
                q.append(c)

    print(max(results))
solution()
