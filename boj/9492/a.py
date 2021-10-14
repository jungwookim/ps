input = __import__('sys').stdin.readline
import sys
def solution():
    n = int(input())
    if n == 0:
        sys.exit()

    a = [input().strip() for _ in range(n)]
    
    if n % 2 == 0:
        a1 = a[:n//2]
        a2 = a[n//2:]
        res = []
        for a1i, a2i in zip(a1, a2):
            res.append(a1i)
            res.append(a2i)
    else:
        a1 = a[:n//2]
        a2 = a[n//2+1:]
        res = []
        for a1i, a2i in zip(a1, a2):
            res.append(a1i)
            res.append(a2i)
        res.append(a[n//2])

    for r in res:
        print(r)
while 1:
    solution()