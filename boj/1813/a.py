input = __import__('sys').stdin.readline

def solution():
    n = int(input())
    a = list(map(int, input().split()))

    l = [0 for _ in range(100005)]

    for i, ai in enumerate(a):
        l[ai] += 1

    for i in range(100004, -1, -1):
        if l[i] == i:
            print(i)
            return

    print(-1)

solution()