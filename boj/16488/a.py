input = __import__('sys').stdin.readline

n, k = map(int, input().split())
print(n*n*k)