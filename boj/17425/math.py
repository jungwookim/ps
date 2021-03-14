input = __import__('sys').stdin.readline


N = 1000000
sums = [0 for _ in range(N + 1)]


def init(n):
    for i in range(1, n + 1):
        for j in range(i, n + 1, i):
            sums[j] += i

        sums[i] += sums[i - 1]
    return sums


def solution():
    n = int(input())
    return sums[n]


sums = init(N)


for _ in range(int(input())):
    print(solution())
