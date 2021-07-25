input = __import__('sys').stdin.readline

def solution():
    n = int(input())
    a = list(map(int, input().split()))
    m = int(input())

    psum0 = [0 for _ in range(n+3)]
    psum1 = [0 for _ in range(n+3)]

    for i, ai in enumerate(a):
        if ai % 2 == 0:
            psum1[i+1] = psum1[i]
            psum0[i+1] += 1 + psum0[i]
        else:
            psum0[i+1] = psum0[i]
            psum1[i+1] += 1 + psum1[i]

    even = []
    odd = []
    for _ in range(m):
        t, l, r = map(int, input().split())
        if t == 1:
            if r % 2 == 1:
                odd.append(l)
            else:
                even.append(l)
            a[l-1] = r
        elif t == 2:
            more = 0
            less = 0
            for e in even:
                if l <= e <= r:
                    more += 1
            for o in odd:
                if l <= o <= r:
                    less -= 1
            print(psum0[r] - psum0[l-1] + more + less)
        elif t == 3:
            more = 0
            less = 0
            for e in odd:
                if l <= e <= r:
                    more += 1
            for o in odd:
                if l <= o <= r:
                    less -= 1
            print(psum1[r] - psum1[l-1] + more + less)

solution()
    