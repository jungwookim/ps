input = __import__('sys').stdin.readline

def solution():
    n = int(input())
    a = tuple(map(int, input().split()))

    
print(*solution())
