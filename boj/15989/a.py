input = __import__('sys').stdin.readline

def solution():
    n = int(input())
    q3 = n // 3

    cnt = 0
    for use3 in range(q3+1):
        r = n - use3 * 3
        use2 = (r // 2) + 1
        cnt += use2

    print(cnt)
for _ in range(int(input())):
    solution()