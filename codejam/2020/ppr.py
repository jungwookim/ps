def solution(cid):
    n = int(input())
    activities = [list(map(int, input().split())) for _ in range(n)]

    def take_first(arr):
        return arr[0]

    def isBetween(s, e, si):
        if s <= si < e:
            return False
        return True

    sorted_activities = sorted(activities, key=take_first)
    j_list = []
    c_list = []
    for sa in sorted_activities:
        si = sa[0]
        ei = sa[1]
        if len(j_list) == 0:
            j_list.append(sa)
            continue
        if len(c_list) == 0:
            c_list.append(sa)
            continue
        if isBetween(j_list[-1][0], j_list[-1][1], si):
            j_list.append(sa)
            continue
        if isBetween(c_list[-1][0], c_list[-1][1], si):
            c_list.append(sa)
            continue

        print('Case #{}: IMPOSSIBLE'.format(cid))
        return

    ans_list = []
    for act in activities:
        if act in j_list:
            ans_list.append('J')
            j_list.remove(act)

        if act in c_list:
            ans_list.append('C')
            c_list.remove(act)
    ans = ''.join(ans_list)
    print('Case #{}: {}'.format(cid, ans))
    return


t = int(input())
for ti in range(t):
    solution(ti + 1)
