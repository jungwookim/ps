input = __import__('sys').stdin.readline

def solution():
    n = int(input())
    a, b = map(int, input().split())
    c = int(input())
    d = [int(input()) for _ in range(n)]

    d.sort(reverse=True)

    maxv = -1
    for i in range(n):
        temp = d[:i]

        price = a + i * b
        cal = c + sum(temp)
        if maxv < (cal // price):
            maxv = cal // price

    print(maxv)
solution()