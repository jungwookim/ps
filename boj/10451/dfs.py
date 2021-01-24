input = __import__('sys').stdin.readline


def dfs(now, edges, visited):
    if visited[now]:
        return

    visited[now] = True
    for next in edges[now]:
        dfs(next, edges, visited)

    return


for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    edges = [[] for _ in range(n)]
    for i, ai in enumerate(a):
        edges[i].append(ai - 1)
    visited = [False for _ in range(n)]
    ans = 0
    for i in range(n):
        if not visited[i]:
            dfs(i, edges, visited)
            ans += 1
    print(ans)
