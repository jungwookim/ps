input = __import__('sys').stdin.readline

def solution():
    n = int(input())
    a = [0 for _ in range(n + 5)]
    
    for i in range(1, n + 1):
        a[i] = a[i-1] + i

    left = 1
    right = 1
    cnt = 0
    while right <= n:
        sumv = a[right] - a[left - 1]
        if sumv < n:
            right += 1
        elif sumv > n:
            left += 1
        else:
            right += 1
            left += 1
            cnt += 1
    print(cnt)
solution()
