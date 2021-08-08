input = __import__('sys').stdin.readline

def solution():
    n = int(input())
    a = list(map(int, input().split()))

    a.sort()

    l = 0
    r = 1

    cnt = 0
    while r <= n-1:
        lv = a[l]
        rv = a[r]
        if l == r:
            r += 1
            continue

        if lv >= 0.9 * rv:
            cnt += (r - l)
            r += 1
        else:
            l += 1
    print(cnt)
solution()