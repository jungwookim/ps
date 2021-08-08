input = __import__('sys').stdin.readline

def solution():
    n = int(input())

    binary = "{0:b}".format(n+1)[1:]
    size = len(binary)
    ans = 0
    for i, b in enumerate(binary):
        if b == '0':
            v = 4
        else:
            v = 7
        ans += v * (10 ** (size-i-1))

    print(ans)
solution()