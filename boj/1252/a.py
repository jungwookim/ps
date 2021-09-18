input = __import__('sys').stdin.readline

a, b = input().strip().split()

print(bin(int(a, 2) + int(b, 2))[2:])
