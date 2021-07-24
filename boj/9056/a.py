input = __import__('sys').stdin.readline

def solution():
    a, b = input().strip().split()
    set_a = set(a)
    set_b = set(b)

    if set_a == set_b:
        print('YES')
    else:
        print('NO')

for i in range(int(input())):
    solution()