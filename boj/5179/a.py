input = __import__('sys').stdin.readline

def solution(cid):
    M, N, P = map(int, input().split())
    p_dict = { i: { problem: { 'count': 0, 'time': 0, 'solved': False } for problem in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'][:M]} for i in range(1, P + 1)}
    for _ in range(N):
        p, m, t, j = input().split()
        p = int(p)
        t = int(t)
        j = int(j)

        if p_dict[p][m]['solved']:
            continue

        if j == 1:
            p_dict[p][m]['time'] = t

        p_dict[p][m]['solved'] = j == 1
        p_dict[p][m]['count'] += 1

    print("Data Set {}:".format(cid + 1))
    ans = [[0, 0, 0] for _ in range(P)]
    for k in p_dict:
        ans[k-1][0] = k
        for k2 in p_dict[k]:
            if p_dict[k][k2]['solved']:
                ans[k-1][1] += 1
                ans[k-1][2] += (0 if p_dict[k][k2]['count'] == 1 else (p_dict[k][k2]['count'] - 1) * 20) + p_dict[k][k2]['time']
    ans.sort(key=lambda x: (-x[1], x[2]))
    for i in ans:
        print(*i)
    print('')


for cid in range(int(input())):
    solution(cid)
