input = __import__('sys').stdin.readline

n = int(input())
binary = "{0:b}".format(n)
size = len(binary)
ans = 0
for i, b in enumerate(binary):
    ans += (0 if b == '0' else 3 ** (size - i - 1))

print(ans)