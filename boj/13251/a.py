input = __import__('sys').stdin.readline

def calc(n, k):
    res = n
    for i in range(k):
        if i >= 1:
            res *= (n-i)
    return res

def solution():
    m = int(input())
    arr = list(map(int, input().split()))
    k = int(input())

    ans = (sum([calc(n, k) for n in arr])) / calc(sum(arr), k)
    print(ans)

solution()
