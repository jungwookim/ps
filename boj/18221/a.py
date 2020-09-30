input = __import__('sys').stdin.readline

def solution():
    n = int(input())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    
    student = [0, 0]
    prof = [0, 0]

    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 2:
                student = [i, j]
            elif matrix[i][j] == 5:
                prof = [i, j]
            else:
                pass



    def distance(a, b):
        ax, ay = a
        bx, by = b
        return ((ax - bx) ** 2 + (ay - by) ** 2) ** 0.5

    if distance(student, prof) < 5:
        print(0)
        return

    cnt = 0
    for i in range(min(student[0], prof[0]), max(student[0], prof[0]) + 1):
        for j in range(min(student[1], prof[1]), max(student[1], prof[1]) + 1):
            if matrix[i][j] == 1:
                cnt += 1

    if cnt >= 3:
        print(1)
    else:
        print(0)

solution()