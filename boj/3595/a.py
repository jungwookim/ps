input = __import__('sys').stdin.readline

def solution():
    n = int(input())

    min_area = float('inf')
    a, b, c = 1, 1, n
    for x in range(1, n + 1):
        if n % x != 0:
            continue
        for y in range(1, n + 1 // x):
            if n % (x * y) != 0:
                continue
            z = n // (x * y)
            area = x * y + y * z + z * x
            if area <= min_area:
                min_area = area
                a, b, c = x, y, z
    print(a, b, c)
solution()