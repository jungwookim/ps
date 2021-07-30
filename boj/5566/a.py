input = __import__('sys').stdin.readline

def solution():
    n, m = map(int, input().split())
    a = [int(input()) for _ in range(n)]
    pos = 1

    for i in range(m):
        x = int(input())
        pos += x
        if pos >= n:
            print(i+1)
            return
        pos += a[pos-1]
        if pos >= n:
            print(i+1)
            return


solution()
    