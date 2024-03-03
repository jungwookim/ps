input = __import__('sys').stdin.readline

def process(ans, add, a, b):
    if a > 0 and b > 0:
        v = min(a, b)
        ans += v * add
        a -= v
        b -= v
    return ans, a, b

def solution():
    n = int(input())
    a = list(map(int, input().split()))

    c3 = a.count(3)
    c2 = a.count(2)
    c1 = a.count(1)
    c0 = a.count(0)
    
    # 0 -> (0, 0), (1, 1), (2, 2), (3, 3)
    # 1 -> (0, 1), (2, 3)
    # 2 -> (0, 2), (1, 3)
    # 3 -> (0, 3), (1, 2)
    ans = 0
    ans, c0, c3 = process(ans, 3, c0, c3)
    ans, c1, c2 = process(ans, 3, c1, c2)
    ans, c0, c2 = process(ans, 2, c0, c2)
    ans, c1, c3 = process(ans, 2, c1, c3)
    ans, c0, c1 = process(ans, 1, c0, c1)
    ans, c2, c3 = process(ans, 1, c2, c3)
    print(ans)


solution()
