input = __import__('sys').stdin.readline

def solution():
    n = int(input())
    ans1 = -1
    ans2 = 1

    for _ in range(n):
        a = list(map(int, input().split()))
        ans1 *= -1 if a[2] == 1 else 1
        ans2 = ans2 // a[0] * a[1]
    print(1 if ans1 == 1 else 0, ans2)

solution()