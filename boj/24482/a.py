input = __import__('sys').stdin.readline
import sys

sys.setrecursionlimit(100000)

def solution():
    n, m, r = map(int, input().split())
    visited = [False for _ in range(n+1)]
    vertex = list(range(n+1))
    edges = [[] for _ in range(n+1)]
    for _ in range(m):
        u, v = map(int, input().split())
        edges[u].append(v)
        edges[v].append(u)


    depths = [-1 for _ in range(n+1)]

    def dfs(v, e, r, prev_depth):
        visited[r] = True
        depths[r] = 1 + prev_depth
        for ei in sorted(edges[r], reverse=True):
            if visited[ei]:
                continue
            else:
                dfs(v, e, ei, depths[r])

    dfs(vertex, edges, r, -1)

    for depth in depths[1:]:
        print(depth)


solution()
