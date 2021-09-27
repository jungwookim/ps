input = __import__('sys').stdin.readline

def solution():
    n = int(input())
    v = [[] for _ in range(n+1)]
    v[1].append(1)
    for _ in range(n-1):
        a, b = map(int, input().split())
        v[a].append(b)
        v[b].append(a)

    parent = [0 for _ in range(n+1)]
    visited = [False for _ in range(n+1)]
    def find_parent(x):
        visited[x] = True
        for c in v[x]:
            if not visited[c]:
                parent[c] = x
                find_parent(c)

    find_parent(1)

    for i in range(2, n+1):
        print(parent[i])

solution()