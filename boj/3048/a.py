input = __import__('sys').stdin.readline

def solution():
    n, m = map(int, input().split())
    a = list(input().strip())
    b = list(input().strip())
    t = int(input())

    aa = [[ai, 1] for ai in a]
    bb = [[bi, -1] for bi in b]
    cc = aa[::-1] + bb

    def move(arr):
        skip_next = False
        for i in range(len(arr)-1):
            if skip_next:
                skip_next = False
                continue
            duo = arr[i:i+2]
            if len(duo) != 2:
                break
            left, right = duo
            lv, ld = left
            rv, rd = right
            if ld != rd and ld == 1:
                arr[i] = right
                arr[i+1] = left
                skip_next = True
        return arr

    for _ in range(t):
        cc = move(cc)

    print(''.join([c for c, _ in cc]))

solution()