input = __import__('sys').stdin.readline

def solution():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))

    for ai in a:
        if ai < x:
            print(ai, end=' ')

solution()