input = __import__('sys').stdin.readline


def solution():
    w, h, x, y, p = map(int, input().split())
    p_list = [list(map(int, input().split())) for _ in range(p)]

    r = h // 2

    def is_in(a, b):
        if (a - (x+w)) ** 2 + (b - (y + r)) ** 2 - r ** 2 <= 0 or (a - x) ** 2 + (b - (y + r)) ** 2 - r ** 2 <= 0 or  y <= b <= y + h and x <= a <= x + w:
            return True
        return False

    ans = 0
    for a, b in p_list:
        if is_in(a, b):
            ans += 1

    print(ans)

solution()
