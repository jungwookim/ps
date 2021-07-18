input = __import__('sys').stdin.readline

def solution():
    a = 'c='
    b = 'c-'
    c = 'dz='
    d = 'd-'
    e = 'lj'
    f = 'nj'
    g = 's='
    h = 'z='
    dic = [a, b, c, d, e, f, g, h]


    s = input().strip()

    skip = 0
    cnt = 0
    for i in range(0, len(s)):
        if skip != 0:
            skip -= 1
            continue
        else:
            if s[i:i+3] in dic:
                skip = 2
            elif s[i:i+2] in dic:
                skip = 1
            cnt += 1

    print(cnt)

solution()
