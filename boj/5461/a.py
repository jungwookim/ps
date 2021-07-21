input = __import__('sys').stdin.readline

def solution():
    n, t, p = map(int, input().split())
    a = [0 for _ in range(t)]
    p_list = [[] for _ in range(n)]
    for ni in range(n):
        results = list(map(int, input().split()))
        for i, r in enumerate(results):
            if r == 0:
                v = 1
            else:
                p_list[ni].append(i)
                v = 0
            a[i] += v
    score = [[0, 0, 0] for _ in range(n)]
    for i, pi in enumerate(p_list):
        score[i][1] += len(pi)
        score[i][2] += i
        for e in pi:
            score[i][0] += a[e]

    target = score[p-1]
    res1 = 0
    res2 = 0
    res3 = 0
    for s in [s for i, s in enumerate(score) if i != p - 1]:
        if s[0] > target[0]:
            res1 += 1
        if s[0] == target[0] and s[1] > target[1]:
            res2 += 1
        if s[0] == target[0] and s[1] == target[1] and s[2] < target[2]:
            res3 += 1
        

    print(target[0], res1 + res2 + res3 + 1)


solution()
