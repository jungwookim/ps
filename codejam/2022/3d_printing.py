def solution(cid):
    target = 10 ** 6
    c1, m1, y1, k1 = map(int, input().split())
    c2, m2, y2, k2 = map(int, input().split())
    c3, m3, y3, k3 = map(int, input().split())

    min_c = min(c1, c2, c3)
    min_m = min(m1, m2, m3)
    min_y = min(y1, y2, y3)
    min_k = min(k1, k2, k3)

    total = min_c + min_m + min_y + min_k
    delta = total - target
    if delta < 0:
        print('Case #{}: IMPOSSIBLE'.format(cid))
        return

    ans = [min_c, min_m, min_y, min_k]
    for i in range(4):
        if delta == 0:
            break
        if ans[i] >= delta:
            ans[i] -= delta
            delta = 0
        else:
            delta -= ans[i]
            ans[i] = 0
    print('Case #{}: {} {} {} {}'.format(cid, ans[0], ans[1], ans[2], ans[3]))
    return

t = int(input())
for ti in range(t):
    solution(ti + 1)
