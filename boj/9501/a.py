def solution():
    n, d = map(int, input().split())
    cnt = 0
    for _ in range(n):
        v, f, c = map(int, input().split())
        if f / c * v >= d:
            cnt += 1
    print(cnt)

for _ in range(int(input())):
    solution()