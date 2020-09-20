input = __import__('sys').stdin.readline

mod = 10 ** 9 + 7

def pow(n, x):
    if x == 0:
        return 1
    
    half = pow(n, x // 2)
    result = (half * half) % mod
    
    if x % 2 == 0:
        return result

    return (result * n) % mod

def solution():
    n = int(input())
    if n == 1:
        return print(1)

    if n == 2:
        return print(1)

    print(pow(2, n - 2))
    

for _ in range(int(input())):
    solution()