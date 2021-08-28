input = __import__('sys').stdin.readline

n, m = map(int, input().split())

parent = list(range(n+1))

def merge(x, y):
    x = find(x)
    y = find(y)
    parent[x] = y

def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]

for _ in range(m):
    t, a, b = map(int, input().split())

    if t == 1:
        # find
        if find(a) == find(b):
            print("YES")
        else:
            print("NO")
    else:
        merge(a, b)
        # merge

