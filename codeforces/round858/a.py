def solution():
    a, b, c, d = map(int, input().split())
    if b - d > 0 or c - a > d - b:
        return -1
    
    dy = d - b
    return dy + (dy + a - c)

for _ in range(int(input())):
    print(solution())
