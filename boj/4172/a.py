input = __import__('sys').stdin.readline
from math import log, sin
import sys
mod = 10**6

a = [1] + [0 for _ in range(mod+2)]
for i in range(1, mod+3):
    a[i] = (a[int(i-i**0.5)] + a[int(log(i))] + a[int(i*(sin(i)**2))]) % mod

def solution():
    n = int(input())
    if n == -1:
        sys.exit()
    print(a[n])

while 1:
    solution()