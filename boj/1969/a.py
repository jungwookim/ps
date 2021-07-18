input = __import__('sys').stdin.readline

def hamming_distance(a, b):
    cnt = 0
    for ai, bi in zip(a, b):
        if ai == bi:
            continue
        else:
            cnt += 1
    return cnt

def solution():
    n, m = map(int, input().split())
    a = [{'A': 0, 'T': 0, 'G': 0, 'C': 0} for _ in range(m)]
    s_list = []
    for i in range(n):
        s = input().strip()
        s_list.append(s)
        for i, char in enumerate(s):
            a[i][char] += 1

    dna = ''
    for ai in a:
        ans = sorted(ai.items(), key=lambda x: (-x[1], x[0]))[0]
        dna += ans[0][0]
    print(dna)
    distance = 0
    for si in s_list:
        distance += hamming_distance(si, dna)
    print(distance)
solution()
