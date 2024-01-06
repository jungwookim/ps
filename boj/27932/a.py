input = __import__('sys').stdin.readline

def solution():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    d = []
    if n == 1:
        d.append(0)
    elif n == 2:
        d.append(abs(a[1] - a[0]))
        d.append(abs(a[1] - a[0]))
    else:
        for i in range(n):
            if i == 0:
                d.append(abs(a[i+1] - a[i]))
            elif i == n-1:
                d.append(abs(a[i-1] - a[i]))
            else:
                d.append(max(abs(a[i+1] - a[i]), abs(a[i-1] - a[i])))

    lt = 0
    rt = max(d)

    def check(x, k):
        cnt = 0
        for di in d:
            if di > x:
                cnt += 1

        return cnt <= k

    ans = rt
    while lt <= rt:
        mid = (lt + rt) // 2

        if check(mid, k):
            rt = mid - 1
            ans = min(mid, ans)
        else:
            lt = mid + 1
    print(ans)
solution()
