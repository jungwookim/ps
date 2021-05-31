input = __import__('sys').stdin.readline

def solution():
    n = int(input())
    a = 100
    b = 100
    for _ in range(n):
        i, j = map(int, input().split())
        if i > j:
            b -= i
        elif i < j:
            a -= j
    print(a)
    print(b)

solution()
