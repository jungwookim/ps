input = __import__('sys').stdin.readline

def solution():
    n = int(input())
    a = [0, 2, 4, 7] + [0] * 100

    add = 3
    for i in range(3, n+1):
        a[i] = a[i-1] + add
        if i % 3 != 0:
            add += 1
    print(a[n])
solution()