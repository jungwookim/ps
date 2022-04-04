def solution(cid):
    n = int(input())
    s = list(map(int, input().split()))
    s.sort()

    cnt = 0
    for si in s:
        if si >  cnt:
            cnt += 1

    print('Case #{}: {}'.format(cid, cnt))
    return

t = int(input())
for ti in range(t):
    solution(ti + 1)
