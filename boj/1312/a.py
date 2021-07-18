input = __import__('sys').stdin.readline

def solution():
    a, b, n = map(int, input().split())
    r = a % b
    q = 0

    while n > 0:
        r *= 10
        q = r // b
        r = r % b
        n -= 1

    print(q)

solution()
