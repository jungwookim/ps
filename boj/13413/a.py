input = __import__('sys').stdin.readline

def solution():
    n = int(input())
    a = input().strip()
    b = input().strip()

    cnt1 = 0
    cnt2 = 0
    for ai, bi in zip(a, b):
        if ai == bi:
            pass
        else:
            if ai == 'W':
                cnt1 += 1
            else:
                cnt2 += 1
    print(min(cnt1, cnt2) + abs(cnt1 - cnt2))
for _ in range(int(input())):
    solution()