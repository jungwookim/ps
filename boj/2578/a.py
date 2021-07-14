input = __import__('sys').stdin.readline

def update(table, q):
    for i in range(len(table)):
        for j in range(len(table)):
            if q == table[i][j]:
                table[i][j] = -1
                return

def result(table):
    cnt = 0
    for row in table:
        if len(set(row)) == 1 and list((set(row)))[0] == -1:
            cnt += 1

    for i in range(len(table)):
        col = []
        for j in range(len(table)):
            col.append(table[j][i])
        
        if len(set(col)) == 1 and list(set(col))[0] == -1:
            cnt += 1

    digonal_cnt_1 = 0
    for i in range(len(table)):
        if table[i][i] == -1:
            digonal_cnt_1 += 1

    if digonal_cnt_1 == 5:
        cnt += 1
    
    digonal_cnt_2 = 0
    for i in range(len(table)):
        if table[i][len(table) - i - 1] == -1:
            digonal_cnt_2 += 1

    if digonal_cnt_2 == 5:
        cnt += 1
    
    return cnt >= 3
def solution():
    n = 5
    matrix = [list(map(int, input().split())) for _ in range(n)]
    queries = [list(map(int, input().split())) for _ in range(n)]

    cnt = 0
    for i in range(n):
        for j in range(n):
            cnt += 1
            q = queries[i][j]

            update(matrix, q)
            if result(matrix):
                print(cnt)
                return

solution()