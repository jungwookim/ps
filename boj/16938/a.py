input = __import__('sys').stdin.readline
from itertools import combinations

def solution():
    n, l, r, x = map(int, input().split())
    ps = list(map(int, input().split()))
    ps.sort()

    cnt = 0
    for i in range(2, n + 1):
        for c in combinations(ps, i):
            total = sum(c)
            if total < l:
                continue
            if total > r:
                continue
            if max(c) - min(c) < x:
                continue
            cnt += 1
    print(cnt)

solution()