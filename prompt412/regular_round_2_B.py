input = __import__('sys').stdin.readline


def solution():
    n = int(input())
    a = []
    for _ in range(n):
        a.append(tuple(map(int, input().split())))

    a.sort(key=lambda x: -x[0])

    current_price = a[0][1]

    filter_out_count = 0
    for _, ci in a[1:]:
        if ci >= current_price:
            filter_out_count += 1
            continue
        current_price = ci

    print(n - filter_out_count)


solution()
