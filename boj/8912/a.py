input = __import__('sys').stdin.readline

def solution():
    n = int(input())
    a = list(map(int, input().split()))

    ans = 0
    for i in range(1, n):
        ans += sum([1 for ai in a[:i] if ai <= a[i]])

    print(ans)

for _ in range(int(input())):
    solution()