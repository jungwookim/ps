input = __import__('sys').stdin.readline

def solution():
    n = int(input())
    a = [list(map(int, input().split())) for _ in range(n)]

    res = float('inf')
    def search(x, y, wsum, cnt, visited):
        nonlocal res
        if cnt == n - 1:
            last_weight = a[y][x]
            if last_weight == 0:
                return
            if res > wsum + last_weight:
                res = wsum + last_weight
            return

        for v, wi in enumerate(a[y]):
            if v == y:
                continue
            if v != x:
                if not visited[v] and wi != 0:
                    visited[v] = True
                    wsum += wi
                    cnt += 1
                    search(x, v, wsum, cnt, visited)
                    visited[v] = False
                    wsum -= wi
                    cnt -= 1


    for i in range(n):
        visited = [False for _ in range(n)]
        search(i, i, 0, 0, visited)
    print(res)
solution()