input = __import__('sys').stdin.readline

n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]

def solution(x, y): # x, y 일 때 움직여서 오른쪽 끝에 도달할 수 있는 경우의 수
    if x >= n or y >= n:
        return 0
    value = matrix[x][y]

    if value == 0:
        return 1
    # 오른쪽으로 이동할 때
    right = solution(x, y + value)
    # 아래로 이동할 때
    down = solution(x + value, y)
    return right + down

print(solution(0, 0))
