input = __import__('sys').stdin.readline

def add_list(a, b):
    result = []
    for ai, bi in zip(a, b):
        result.append(ai + bi)

    return result

def sub_list(a, b):
    result = []
    for ai, bi in zip(a, b):
        result.append(ai - bi)

    return result    
def solution():
    n = int(input())
    matrix = []
    for _ in range(n):
        row = list(map(int, input().split()))
        matrix.append(row)

    partial_set = [[[0 for _ in range(10)] for _ in range(n + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            partial_set[i][j][matrix[i-1][j-1] - 1] += 1
            partial_set[i][j] = add_list(partial_set[i][j], partial_set[i][j-1])
            partial_set[i][j] = add_list(partial_set[i][j], partial_set[i-1][j])
            partial_set[i][j] = sub_list(partial_set[i][j], partial_set[i-1][j-1])

    for _ in range(int(input())):
        x1, y1, x2, y2 = map(int, input().split())
        res = sub_list(partial_set[x2][y2], partial_set[x2][y1-1])
        res = sub_list(res, partial_set[x1-1][y2])
        res = add_list(res, partial_set[x1-1][y1-1])
        print(len([ri for ri in res if ri > 0]))
solution()
