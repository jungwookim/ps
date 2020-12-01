input = __import__('sys').stdin.readline

def solution():
    a = [int(input()) for _ in range(int(input()))]
    a.sort()

    for ai in a:
        print(ai)

solution()
