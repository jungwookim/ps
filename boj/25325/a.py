input = __import__('sys').stdin.readline

def solution():
    n = int(input())
    a = input().split()

    res = {}
    for ai in a:
        res[ai] = 0
    
    for _ in range(n):
        for s in input().split():
            res[s] += 1
    
    for k, v in sorted(res.items(), key=lambda x: -x[1]):
        print(k, v)

solution()
