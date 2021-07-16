input = __import__('sys').stdin.readline

def solution():
    j, n = map(int, input().split())
    a = [e[0] * e[1] for e in [list(map(int, input().split())) for _ in range(n)]]

    a.sort(reverse=True)

    cnt = 0
    for ai in a:
        j = j - ai
        cnt += 1
        if j <= 0:
            break
    print(cnt)

for _ in range(int(input())):
    solution()