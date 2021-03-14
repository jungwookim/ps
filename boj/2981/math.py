input = __import__('sys').stdin.readline


def calc_gcd(a, b):
    if b > a:
        a, b = b, a
    while b != 0:
        a, b = b, a % b
    return a


def solution():
    n = int(input())
    a = []
    for _ in range(n):
        a.append(int(input()))

    a.sort()

    gcd = a[1] - a[0]
    for i in range(1, n - 1):
        gcd = calc_gcd(gcd, a[i + 1] - a[i])

    divisors = []
    for i in range(1, int(gcd ** (0.5)) + 1):
        if gcd % i == 0:
            divisors.append(i)
            if i != gcd // i:
                divisors.append(gcd // i)

    divisors.sort()

    print(*divisors[1:])


solution()
