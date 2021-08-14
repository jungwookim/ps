input = __import__('sys').stdin.readline
from math import factorial

def nCr(n, r):
    return factorial(n) // (factorial(r) * factorial(n-r))
def solution():
    n = int(input())
    m = int(input())

    def nHr(n, r):
        return nCr(n+r-1, r)

    if n <= m:
        print(nHr(n, m-n))
    else:
        print(nCr(n, m))
solution()