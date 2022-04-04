def solution(cid):
    r, c = map(int, input().split())
    
    matrix = [["." for _ in range(c * 2 + 1)] for _ in range(r * 2 + 1)]

    for i in range(r * 2 + 1):
        for j in range(c * 2 + 1):
            if i % 2 == 0 and j % 2 == 0:
                matrix[i][j] = "+"
                continue
            if i % 2 == 1 and j % 2 == 0:
                matrix[i][j] = "|"
                continue
            if i % 2 == 0 and j % 2 == 1:
                matrix[i][j] = "-"
                continue
    matrix[0][0] = "."
    matrix[0][1] = "."
    matrix[1][0] = "."

    print('Case #{}:'.format(cid))
    for row in matrix:
        print("".join(row))
    return

t = int(input())
for ti in range(t):
    solution(ti + 1)
