input = __import__('sys').stdin.readline

def solution():
    n, q = map(int, input().split())
    n = [0 for _ in range(n + 1)]
    n[0] = 1

    for _ in range(q):
        x, y = map(int, input().split())
        i = 0
        while 1:
            try:
                n[x + y * i] = 1
                i += 1
            except:
                break
    print(n.count(0))

solution()
