input = __import__('sys').stdin.readline
from math import gcd

def solution():
    n, m = map(int, input().split())

    val = gcd(n, m)

    for i in range(1, val + 1):
        if n % i == 0 and m % i == 0:
            print(i, n // i, m // i)

solution()
