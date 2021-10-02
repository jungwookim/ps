input = __import__('sys').stdin.readline

def solution():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()

    cnt = n
    for i in range(n):
        temp = a[i] + n - (i + 1)
        if temp < cnt:
            cnt = temp

    print(cnt)

solution()