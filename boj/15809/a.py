input = __import__('sys').stdin.readline

def solution():
    n, m = map(int, input().split())
    power = [int(input()) for _ in range(n)]
    parent = [i for i in range(n)]

    def find(x):
        if x == parent[x]:
            return x
        parent[x] = find(parent[x])

        return parent[x]

    def union(x, y):
        x = find(x)
        y = find(y)

        parent[x] = y
        
    def fight(x, y):
        x = find(x)
        x_power = sum([power[i] for i, pi in enumerate(parent) if find(pi) == find(x)])
        y = find(y)
        y_power = sum([power[i] for i, pi in enumerate(parent) if find(pi) == find(y)])
        if x_power >= y_power:
            update_once = False
            for i, pi in enumerate(parent):
                if find(pi) == find(x):
                    if not update_once:
                        update_once = True
                        power[i] = x_power - y_power
                    else:
                        power[i] = 0
                if find(pi) == find(y):
                    power[i] = 0
            union(y, x)
        else:
            update_once = False
            for i, pi in enumerate(parent):
                if find(pi) == find(y):
                    if not update_once:
                        update_once = True
                        power[i] = y_power- x_power
                    else:
                        power[i] = 0
                if find(pi) == x:
                    power[i] = 0
            union(x, y)
        
    for _ in range(m):
        o, p, q = map(int, input().split())
        p -= 1
        q -= 1
        if o == 1:
            union(p, q)
        else:
            fight(p, q)

    power_dict = {}
    for i in range(n):
        if power[i] > 0:
            group = find(parent[i])
            if group in power_dict:
                power_dict[group] += power[i]
            else:
                power_dict[group] = power[i]
    print(len(power_dict))
    print(*sorted(power_dict.values()))



solution()