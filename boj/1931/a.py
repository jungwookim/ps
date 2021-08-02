input = __import__('sys').stdin.readline

def solution():
    n = int(input())
    a = [list(map(int, input().split())) for _ in range(n)]

    a.sort(key = lambda x: (x[1], x[0]))

    left, right = a[0]
    cnt = 1
    for i, ai in enumerate(a):
        if i != 0 :
            next_left, next_right = a[i]
            if next_left < right:
                continue
            else:
                cnt += 1
                left = next_left
                right = next_right
    print(cnt)
solution()