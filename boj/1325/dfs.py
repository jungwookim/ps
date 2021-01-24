input = __import__('sys').stdin.readline

limit = 100005
nodes = [[] for _ in range(limit)]
while True:
    node = list(map(int, input().split()))
    if not node:
        break

    nodes[node[1]].append(node[0])

def solution(now):
    visited = [False for _ in range(limit)]
    def dfs(now):
        if visited[now]:
            return

        visited[now] = True
        for next_index in nodes[now]:
            dfs(next_index)
    dfs(now)
    return visited.count(True)

cnt_arr = []
idx_arr = []
for i, node in enumerate(nodes):
    if len(node) != 0:
        cnt_arr.append(solution(i))
        idx_arr.append(i)

maxv = max(cnt_arr)
ans = []
for i, cnt in enumerate(cnt_arr):
    if cnt == maxv:
        ans.append(idx_arr[i])

print(*ans)
