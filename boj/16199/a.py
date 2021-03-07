input = __import__('sys').stdin.readline


def solution():
    y1, m1, d1 = map(int, input().split())
    y2, m2, d2 = map(int, input().split())

    y = y2 - y1
    m = m2 - m1
    d = d2 - d1

    if y > 0:
        if m > 0:
            print(y)
        elif m == 0:
            if d >= 0:
                print(y)
            else:
                print(y - 1)
        else:
            print(y - 1)
    else:
        if m > 0:
            print(y)
        elif m == 0:
            if d >= 0:
                print(y)
            else:
                print(y - 1)
        else:
            print(y - 1)
    print(y + 1)
    print(y)


solution()
