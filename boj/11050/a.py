input = __import__('sys').stdin.readline

def factorial(n):
    a = 1
    for i in range(1, n + 1):
        a *= i
    return a

def solution():
    n, k = map(int, input().split())
    print(factorial(n) // (factorial(n-k) * factorial(k)))

solution()
