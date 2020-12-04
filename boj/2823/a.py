input = __import__('sys').stdin.readline

def solution():
    n, m = map(int, input().split())
    base_map = [['X' for _ in range(m + 2)] for _ in range(n + 2)]
    temp_map = [input().strip() for _ in range(n)]

    for i in range(n):
        for j in range(m):
            base_map[i + 1][j + 1] = temp_map[i][j]


    def countAdjacent(a, b):
        cnt = 0
        if base_map[a + 1][b] == '.':
            cnt += 1
        if base_map[a - 1][b] == '.':
            cnt += 1
        if base_map[a][b + 1] == '.':
            cnt += 1
        if base_map[a][b - 1] == '.':
            cnt += 1

        return cnt

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            current = base_map[i][j]

            if current == '.':
                if countAdjacent(i, j) >= 2:
                    pass
                else:
                    return print(1)
            else:
                pass

    return print(0)

solution()
            