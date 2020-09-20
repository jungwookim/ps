input = __import__('sys').stdin.readline

def func(method, matrix):
    row_size = len(matrix[0])
    col_size = len(matrix)

    if method == 1:
        new_matrix = [[0 for _ in range(row_size)] for _ in range(col_size)]
        for i in range(row_size):
            for j in range(col_size):
                new_matrix[j][i] = matrix[-(j+1)][i]
    elif method == 2:
        new_matrix = [[0 for _ in range(row_size)] for _ in range(col_size)]
        for i in range(row_size):
            for j in range(col_size):
                new_matrix[j][i] = matrix[j][-(i+1)]
    elif method == 3:
        new_matrix = [[0 for _ in range(col_size)] for _ in range(row_size)]
        for i in range(row_size):
            for j in range(col_size):
                new_matrix[i][-(j+1)] = matrix[j][i]
    elif method == 4:
        new_matrix = [[0 for _ in range(col_size)] for _ in range(row_size)]
        for i in range(row_size):
            for j in range(col_size):
                new_matrix[-(i+1)][j] = matrix[j][i]
    elif method == 5:
        new_matrix = [[0 for _ in range(row_size)] for _ in range(col_size)]
        for j in range(col_size): # 0 ~ 5
            for i in range(row_size): # 0~7
                row_line = row_size // 2 # 4
                col_line = col_size // 2 # 3
                cell = matrix[j][i]
                if i < row_line and j < col_line: # 1
                    new_matrix[j][i + row_line] = cell
                elif i >= row_line and j < col_line: # 2
                    new_matrix[j + col_line][i] = cell
                elif i >= row_line and j >= col_line: # 3
                    new_matrix[j][i - row_line] = cell
                else: # 4
                    new_matrix[j - col_line][i] = cell

    elif method == 6:
        new_matrix = [[0 for _ in range(row_size)] for _ in range(col_size)]
        for j in range(col_size): # 0 ~ 5
            for i in range(row_size): # 0~7
                row_line = row_size // 2 # 4
                col_line = col_size // 2 # 3
                cell = matrix[j][i]
                if i < row_line and j < col_line: # 1 to 4
                    new_matrix[j + col_line][i] = cell
                elif i >= row_line and j < col_line: # 2 to 1
                    new_matrix[j][i - row_line] = cell
                elif i >= row_line and j >= col_line: # 3 to 2
                    new_matrix[j - col_line][i] = cell
                else: # 4 to 3
                    new_matrix[j][i + row_line] = cell
    return new_matrix

def print_matrix(matrix):
    for row in matrix:
        for cell in row:
            print(cell, end=' ')
        print()

def solution():
    n, _, _ = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    rs = list(map(int, input().split()))
    for method in rs:
        matrix = func(method, matrix)
    print_matrix(matrix)

solution()
