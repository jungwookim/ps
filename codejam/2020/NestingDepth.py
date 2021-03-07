def solution(cid):
    n = str(input())
    d_list = list(set([int(d) for d in n]))
    left_cnt = 0
    right_cnt = 0

    ans = []
    for i, d in enumerate(n):
        if i == 0:
            ans += ['(' for _ in range(int(d))]
            ans += [d]
            left_cnt += int(d)
            continue

        if left_cnt == int(d):
            ans += [d]
            pass
        elif left_cnt < int(d):
            ans += ['(' for _ in range(int(d) - left_cnt)]
            ans += [d]
            left_cnt += int(d) - left_cnt
        else:
            ans += [')' for _ in range(left_cnt - int(d))]
            ans += [d]
            left_cnt -= left_cnt - int(d)
            right_cnt += left_cnt - int(d)
    else:
        ans += [')' for _ in range(left_cnt - right_cnt)]
        right_cnt += left_cnt - right_cnt

    print('Case #{}: {}'.format(cid, ''.join(ans)))
    return


t = int(input())
for ti in range(t):
    solution(ti + 1)
