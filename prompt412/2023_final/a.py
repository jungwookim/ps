input = __import__('sys').stdin.readline

def solution():
    n = int(input())
    a = []
    for _ in range(n):
        ai, bi = map(int, input().split())
        a.append((ai, bi, ai - bi))

    a.sort(key = lambda x : (x[2], -x[1]))
    partial = [0]
    for ai in a:
        x, y, _ = ai
        partial.append(partial[-1] + y)

    ans = float("-inf")
    for i, ai in enumerate(a):
        x, y, _ = ai
        ans = max(ans, x - partial[i + 1])
    print(ans)

solution()
