input = __import__('sys').stdin.readline

def solution():
    current = 0
    res = 0
    for _ in range(10):
        o, i = map(int, input().split())
        add = i - o
        current += add
        res = max(current, res)

    print(res)

solution()