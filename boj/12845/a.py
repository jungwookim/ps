input = __import__('sys').stdin.readline

def solution():
    n = int(input())
    a = list(map(int, input().split()))

    print(sum(a) + max(a) * (n-2))

solution()