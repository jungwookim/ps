def solution():
    n = int(input())
    magic = n * (n ** 2 + 1) // 2
    matrix = [list(map(int, input().split())) for _ in range(n)]

    # check duplication
    cells = set()
    for i in range(n):
        for j in range(n):
            cell = matrix[i][j]
            if cell in cells:
                print('FALSE')
                return
            cells.add(cell)

    def checkMagic(arr):
        return sum(arr) == magic

    # check row
    for row in matrix:
        if not checkMagic(row):
            print('FALSE')
            return

    # check column
    for i in range(n):
        col = []
        for j in range(n):
            col.append(matrix[i][j])
        if not checkMagic(col):
            print('FALSE')
            return

    # check digonal
    dig_1 = []
    dig_2 = []
    for i in range(n):
        for j in range(n):
            if i == j:
                dig_1.append(matrix[i][j])
            if i + j == n - 1:
                dig_2.append(matrix[i][j])

    if not checkMagic(dig_1) or not checkMagic(dig_2):
        print('FALSE')
        return

    print('TRUE')

solution()
