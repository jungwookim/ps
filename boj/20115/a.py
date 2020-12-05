input = __import__('sys').stdin.readline

def calc(x, y):
    if x >= y:
        return x + y / 2
    return x / 2 + y

def solution():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort(reverse=True)

    ans = calc(a[0], a[1])
    for i in range(2, n):
        ans = calc(ans, a[i])

    print(ans)

solution()
