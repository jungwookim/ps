input = __import__('sys').stdin.readline


def calc_gcd(a, b):
    if b > a:
        a, b = b, a
    while b != 0:
        a, b = b, a % b
    return a


def solution():
    n, m = map(int, input().split())
    used_matrix = [[0 for _ in range(2005)] for _ in range(2005)]
    ans = 0
    for i in range(n, m + 1):
        for j in range(1, i + 1):
            gcd = calc_gcd(i, j)
            if used_matrix[i // gcd][j // gcd] == 0:
                used_matrix[i // gcd][j // gcd] = 1
                ans += 1

    print(ans)


solution()
