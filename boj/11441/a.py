input = __import__('sys').stdin.readline

def solution():
    n = int(input())
    a = list(map(int, input().split()))
    partial_sum = [0 for _ in range(n+1)]

    for i in range(n):
        partial_sum[i+1] += partial_sum[i] + a[i]
    

    m = int(input())
    for _ in range(m):
        l, r  = map(int, input().split())
        print(partial_sum[r] - partial_sum[l - 1])

solution()