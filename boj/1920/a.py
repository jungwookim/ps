input = __import__('sys').stdin.readline

def solution():
    n = int(input())
    a = list(map(int, input().split()))
    m = int(input())
    b = list(map(int, input().split()))

    a_set = set(a)

    for bi in b:
        if bi in a_set:
            print(1)
        else:
            print(0)

solution()
