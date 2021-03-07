input = __import__('sys').stdin.readline


def solution():
    n = int(input())

    i = 1

    ans = 0
    while True:
        if n == 0:
            print(ans)
            break

        if n - i < 0:
            i = 1

        n -= i
        i += 1
        ans += 1


solution()
