input = __import__('sys').stdin.readline
import math
def solution():
    r, c = map(int, input().split())
    a = list(map(int, input().split()))
    p = list(map(int, input().split()))

    mod = 998244353
    
    print((math.factorial(r * c) // math.factorial(r)) % mod)

solution()

    