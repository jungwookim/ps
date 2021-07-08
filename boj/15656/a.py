from itertools import product
n, m = map(int, input().split())
a = list(map(int, input().split()))

a.sort()
for item in product(a, repeat=m):
    print(*item)
