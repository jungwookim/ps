input = __import__('sys').stdin.readline

def solution():
    n, m = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(n)]

    psum = [[0 for _ in range(m+1)] for _ in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, m+1):
            psum[i][j] = psum[i][j-1] + psum[i-1][j] - psum[i-1][j-1] + matrix[i-1][j-1]

    k = int(input())
    for _ in range(k):
        x1, y1, x2, y2 = map(int, input().split())
        value = psum[x2][y2] - psum[x1-1][y2] - psum[x2][y1-1] + psum[x1-1][y1-1]
        print(value)

solution()
