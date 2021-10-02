input = __import__('sys').stdin.readline

def solution():
    m = int(input())
    matrix = []
    a = set()
    cols = [[] for _ in range(m)]
    for _ in range(m):
        row = list(map(int, input().split()))
        matrix.append(row)
        a.add(sum(row))
        for i, c in enumerate(row):
            cols[i].append(c)

    for col in cols:
        a.add(sum(col))
    diagonal1 = 0
    diagonal2 = 0
    for i in range(m):
        for j in range(m):
            if i == j:
                diagonal1 += matrix[i][j]
            if i + j == m - 1:
                diagonal2 += matrix[i][j]
    a.add(diagonal1)
    a.add(diagonal2)
    if len(a) == 1:
        print("Magic square of size {}".format(m))
    else:
        print("Not a magic square")

for _ in range(int(input())):
    solution()