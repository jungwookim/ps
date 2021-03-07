def solution(cid):
    n = int(input())
    matrix = [list(map(int, input().split())) for _ in range(n)]

    r = 0
    c = 0
    k = 0
    for row in matrix:
        if len(set(row)) < len(row):
            r += 1

    for i in range(n):
        for j in range(n):
            if i == j:
                k += matrix[i][j]
                continue

    for j in range(n):
        col = []
        for i in range(n):
            if matrix[i][j] not in col:
                col.append(matrix[i][j])
                continue
            c += 1
            break

    print('Case #{}: {} {} {}'.format(cid, k, r, c))
    return


t = int(input())
for ti in range(t):
    solution(ti + 1)
