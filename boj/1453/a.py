input = __import__('sys').stdin.readline

def solution():
    n = int(input())
    a = list(map(int, input().split()))

    used = [False for _ in range(100)]

    ans = 0
    for ai in a:
        if used[ai-1]:
            ans += 1
        else:
            used[ai-1] = True

    print(ans)
solution()