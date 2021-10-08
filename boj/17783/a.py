input = __import__('sys').stdin.readline

def solution():
    n = int(input())
    if n % 2 == 0:
        print("Alice")
        print(n-1)
    else:
        print("Bob")

solution()