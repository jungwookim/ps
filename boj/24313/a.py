input = __import__('sys').stdin.readline

def solution():
    a1, a0 = map(int, input().split())
    c = int(input())
    n = int(input())

    if c < a1:
        print(0)
    else:
        if a1 * n + a0 <= c * n:
            print(1)
        else:
            print(0)

solution()
