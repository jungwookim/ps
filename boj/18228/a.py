input = __import__('sys').stdin.readline

def solution():
    n = int(input())
    a = list(map(int, input().split()))

    target = a.index(-1)

    left = a[:target]
    right = a[target+1:]

    print(min(left) + min(right))

solution()