input = __import__('sys').stdin.readline

def solution():
    _a = list(input().strip())
    prev = _a[0]
    a = [prev]
    for ai in _a[1:]:
        if ai == prev:
            pass
        else:
            a.append(ai)
            prev = ai
    a = list(map(lambda x: x.upper(), a))
    n = int(input())
    l = list(map(int, input().split()))
    dic = {}
    for j, i in enumerate(range(ord('A'), ord('Z') + 1)):
        dic[chr(i)] =  l[j]
    cnt_space = a.count(' ')
    if cnt_space > n:
        print(-1)
        return

    flag = True
    res = ''
    for ai in a:
        if ai == ' ':
            flag = True
        elif flag:
            res += ai
            dic[ai] -= 2
            flag = False
        else:
            dic[ai] -= 1

    for k, v in dic.items():
        if v < 0:
            print(-1)
            return

    print(res)
    

solution()
    