input = __import__('sys').stdin.readline

def solution():
    n = int(input())
    a = list(map(int, input().split()))

    print(min(a), max(a))

for _ in range(int(input())):
    solution()