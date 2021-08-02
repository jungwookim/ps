input = __import__('sys').stdin.readline

def solution():
    a = input().strip()

    d = []
    for i in range(len(a)):
        d.append(a[i:] + a[:i])

    d.sort()

    print(d[0])
for _ in range(int(input())):
    solution()
