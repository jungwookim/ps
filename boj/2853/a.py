
def solution():
    n = int(input())
    delta = []
    one = int(input())
    for i in range(1, n):
        delta.append(int(input()) - 1)

    visited = [False for _ in range(n - 1)]
    cnt = 0
    for i, di in enumerate(delta):
        if visited[i]:
            continue
        cnt += 1
        visited[i] = True
        for j, dj in enumerate(delta[i+1:]):
            if dj % di == 0:
                visited[i + 1 + j] = True

    print(cnt)

solution()