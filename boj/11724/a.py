input = __import__('sys').stdin.readline

def solution():
    n, m = map(int, input().split())
    nodes = [n for i in range(1, n+1)]
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)


    visited = [False for _ in range(n+1)]
    def search(x):
        if visited[x]:
            return

        visited[x] = True
        for n in graph[x]:
            search(n)

    cnt = 0
    for i in range(1, n+1):
        if not visited[i]:
            search(i)
            cnt += 1
    print(cnt)
solution()