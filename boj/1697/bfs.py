input = __import__('sys').stdin.readline

limit = 100001


def is_valid_range(a):
    if 0 <= a <= limit - 1:
        return True
    return False


def solution():
    n, m = map(int, input().split())

    if n >= m:
        print(n - m)
        return

    # init
    edges = [[] for _ in range(limit)]
    for i in range(limit):
        if is_valid_range(i + 1):
            edges[i].append(i + 1)
        if is_valid_range(i - 1):
            edges[i].append(i - 1)
        if is_valid_range(i * 2):
            edges[i].append(i * 2)

    q = []
    visited = [False for _ in range(limit)]

    q.append((n, 0))
    visited[n] = True

    while len(q):
        now_index, depth = q.pop(0)
        if now_index == m:
            print(depth)
            return

        for next_index in edges[now_index]:
            if visited[next_index]:
                continue
            visited[next_index] = True
            q.append((next_index, depth + 1))


solution()
