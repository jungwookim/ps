input = __import__('sys').stdin.readline

def solution():
    b1, b2 = map(int, input().split())
    d1, d2 = map(int, input().split())
    j1, j2 = map(int, input().split())

    d = abs(d1 - j1) + abs(d2 - j2)

    b_temp_1 = abs(b1 - j1)
    b_temp_2 = abs(b2 - j2)

    b = 0

    if b_temp_1 > b_temp_2:
        b = b_temp_1
    elif b_temp_1 < b_temp_2:
        b = b_temp_2
    else:
        b = b_temp_1

    if d == b:
        print('tie')
    elif d > b:
        print('bessie')
    else:
        print('daisy')

solution()
