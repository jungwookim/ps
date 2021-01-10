input = __import__('sys').stdin.readline

n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
table = [[0 for _ in range(n + 10)] for _ in range(n + 10)]

def solution(x, y): # x, y 일 때 움직여서 오른쪽 끝에 도달할 수 있는 경우의 수
    if x >= n or y >= n:
        return
    value = matrix[x][y]

    if value == 0:
        if x == n - 1 and y == n - 1:
            table[x][y] += 1
        return
    # 오른쪽으로 이동할 때
    right = table[x][y + value]
    # 아래로 이동할 때
    down = table[x + value][y]
    table[x][y] = right + down

for i in reversed(range(n)):
    for j in reversed(range(n)):
        solution(i, j)


print(table[0][0])
