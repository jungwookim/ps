input = __import__('sys').stdin.readline
from itertools import product
from functools import reduce

def solution():
    n = int(input())
    a = list(map(int, input().split()))

    target = reduce(lambda x, y: x * y, a)

    for bi in product(range(1, 10), repeat=n):
        if reduce(lambda x, y: x * y, bi) > target:
            print(*bi)
            break
    else:
        print(-1)
solution()