input = __import__('sys').stdin.readline

def solution():
    n = int(input())
    a = list(map(int, input().split()))
    p = list(range(1, n+1))

    for i in range(n):
        x = a[-i-1]
        p = p[:x] + [p[-1]] + p[x:-1]

    print(*p)
solution()