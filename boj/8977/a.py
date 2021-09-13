input = __import__('sys').stdin.readline

def solution():
    n, k, b = map(int, input().split())
    a = list(map(int, input().split())) * 2
    _, start = divmod(b, n)
    q, r = divmod(k, n)
    if start == 0:
        start = n
    print(sum(a[:n]) * q + sum(a[start-1:start-1+r]))

solution()