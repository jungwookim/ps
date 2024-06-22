input = __import__('sys').stdin.readline

def solution():
    n, k = map(int, input().split())

    size = 1002
    m = [[0 for _ in range(size)] for _ in range(size)]

    for _ in range(n):
        x1, y1, x2, y2 = map(int, input().split())
        m[x1][y1] += 1
        m[x1][y2] -= 1
        m[x2][y1] -= 1
        m[x2][y2] += 1

    for i in range(size):
        for j in range(1, size):
            m[i][j] += m[i][j-1]

    for j in range(size):
        for i in range(1, size):
            m[i][j] += m[i-1][j]

    cnt = 0
    for ei in m:
        for ej in ei:
            if k == ej:
                cnt += 1
    print(cnt)

solution()