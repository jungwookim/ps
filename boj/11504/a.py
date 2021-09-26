input = __import__('sys').stdin.readline

def solution():
    n, m = map(int, input().split())
    _x = input().strip().split()
    _y = input().strip().split()
    a = list(map(int, input().split()))
    b = a * 9

    x = int(''.join(_x))
    y = int(''.join(_y))
    cnt = 0
    for i in range(n):
        v = int(''.join(map(str, b[i:i+m])))
        if x <= v <= y:
            cnt += 1
    print(cnt)
for _ in range(int(input())):
    solution()