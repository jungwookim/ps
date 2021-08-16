input = __import__('sys').stdin.readline

def solution():
    n = int(input())
    x = list(map(int, input().split()))

    x_set = sorted(list(set(x)))
    x_dict = { xi: i for i, xi in enumerate(x_set) }

    for xi in x:
        print(x_dict[xi], end=' ')

solution()