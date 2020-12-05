input = __import__('sys').stdin.readline

def solution():
    n = int(input())

    cnt = 0
    while True:
        res = n % 2
        if res == 1:
            break
        n = n // 2
        cnt += 1

    print(64 - cnt)

solution()
