input = __import__('sys').stdin.readline

def solution():
    n = int(input())
    a = sorted(list(map(int, input().split())))

    if n % 2 == 0:
        print(sum(a[n//2:]) * 2)
    else:
        print(sum(a[n//2+1:]) * 2 + a[n//2])

solution()