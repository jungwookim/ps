input = __import__('sys').stdin.readline

def solution():
    n = int(input())

    for _ in range(n):
        a = input().strip().split()
        a[0] = a[0][0].upper() + a[0][1:]
        print(*a)

solution()