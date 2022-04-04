input = __import__('sys').stdin.readline

def solution():
    n = int(input())
    stack = []
    counts = {}
    points = {}
    for i in range(1, n+1):
        a = list(map(int, input().split()))
        if len(a) != 1:
            _, point, t = a
            counts[i] = t
            points[i] = point
            for _ in range(t):
                stack.append([i, point, t])


    for _ in range(n):
        i, _, _ = stack.pop()
        counts[i] -= 1

    result = 0
    for i, v in counts.items():
        if v == 0:
            result += points[i]
    print(result)

solution()
