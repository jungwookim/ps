input = __import__('sys').stdin.readline

def solution():
    n = int(input())
    w = []
    c = []
    a = []
    for _ in range(n):
        a.append(list(map(float, input().split())))

    a.sort(key=lambda x: (x[0], -x[-1]))

    candi = []
    cnt = 1
    init_c = a[0][1]
    init_w = a[0][0]
    print('###', a)
    for ai in a[1:]:
        if init_c > ai[1]:
            print('count', ai)
            init_c = ai[1]
            cnt += 1
        elif init_c < ai[1]:
            print('no count', ai)
            continue
        else:
            if init_w == ai[0]:
                candi.append(cnt)
                print('>>>', ai)
                continue
            cnt += 1
    else:
        candi.append(cnt)

    print(candi)
    print(max(candi))

    
for _ in range(int(input())):
    solution()
