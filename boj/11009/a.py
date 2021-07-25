input = __import__('sys').stdin.readline

def solution():
    n, m = map(int, input().split())
    matrix = [[-1 for _ in range(n+m+1)] for _ in range(n+m+1)]

    def f(a, b):
        if b == 1:
            matrix[a][a + b] = 1
            return a / (a+b)
        sumv = a + b
        matrix[a][b] = (a / sumv) + matrix[a][b-1] * b / sumv
        return (a / sumv) + (b / sumv) * (b-1 / sumv) * f(a, b-1)
    
    for i in range(1, n+1):
        for j in range(1, m+1):
            f(i, j)
    print(matrix)
    return f(n, m)

for _ in range(int(input())):
    print(solution())