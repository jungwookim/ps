input = __import__('sys').stdin.readline

def solution():
    n = int(input())
    a, b = map(int, input().split())
    m = int(input())

    parents = [i for i in range(n+1)]
    for _ in range(m):
        x, y = map(int, input().split())
        parents[y] = x

    parents_list = [[i] for i in range(n+1)]
    def make_parent_list(x):
        p = parents[x]
        if x != p:
            parents_list[x].append(p)
        while True:
            if parents[p] == p:
                break
            else:
                p = parents[p]
                parents_list[x].append(p)


    for i in range(1, n+1):
        make_parent_list(i)
    parents_a = parents_list[a]
    parents_b = parents_list[b]


    for i, ai in enumerate(parents_a):
        for j, bj in enumerate(parents_b):
            if ai == bj:
                print(i+j)
                return
    else:
        print(-1)
solution()