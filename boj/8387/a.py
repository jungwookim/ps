input = __import__('sys').stdin.readline

def solution():
    n = int(input())
    a = input().strip()
    b = input().strip()

    cnt = 0
    for ai, bi in zip(a, b):
        if ai == bi:
            cnt += 1

    print(cnt)

solution()