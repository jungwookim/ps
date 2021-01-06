input = __import__('sys').stdin.readline

def solution():
    n = 10

    a = []
    b = []
    for i in range(2*n):
        if i < 10:
            a.append(int(input()))
        else:
            b.append(int(input()))

    a.sort(reverse=True)
    b.sort(reverse=True)

    print(sum(a[:3]), sum(b[:3]))

solution()
    