input = __import__('sys').stdin.readline

def solution():
    n, m = map(int, input().split())
    
    profits = []
    costs = []
    
    for _ in range(n):
        pi, ci = map(int, input().split())
        profits.append(pi)
        costs.append(ci)


    l = 1
    r = 10**10
    def calc(day):
        sumv = 0
        for i in range(n):
            c = costs[i]
            p = profits[i]

            v = p * day - c
            if v > 0:
                sumv += v
        return sumv >= m
                
    while l <= r:
        mid = (l + r) // 2

        if calc(mid):
            r = mid - 1
            ans = mid
        else:
            l = mid + 1
    print(ans)

solution()