input = __import__('sys').stdin.readline

def solution(cid):
    a = input().strip()
    b = input().strip()

    a_dic = {}
    b_dic = {}

    for ai in a:
        if ai in a_dic:
            a_dic[ai] += 1
        else:
            a_dic[ai] = 1

    for bi in b:
        if bi in b_dic:
            b_dic[bi] += 1
        else:
            b_dic[bi] = 1


    keys = set(a_dic.keys()).union(set(b_dic.keys()))

    ans = 0
    for k in keys:
        if k not in a_dic:
            a_dic[k] = 0
        if k not in b_dic:
            b_dic[k] = 0
        ans += abs(a_dic[k] - b_dic[k])
    print("Case #{}: {}".format(cid, ans))
for i in range(int(input())):
    solution(i + 1)