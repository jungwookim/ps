from itertools import combinations
def solution():
    n = int(input())
    matrix = []
    for _ in range(n):
        matrix.append(list(map(int, input().split())))

    print(matrix)
    total_sum = 0
    for row in matrix:
        for cell in row:
            total_sum += cell

    print('sum', total_sum)
    temp = []
    for i in range(2, n):
        results = combinations(list(range(0, n)), i)
        for r in results:
            score = 0
            for ri in r:
                for rj in r:
                    score += matrix[ri][rj]
            print('set', r)
            print('score', score)
            other_score = total_sum - score
            temp.append(abs(other_score - score))


    print(temp)

solution()