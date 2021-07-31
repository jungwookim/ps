input = __import__('sys').stdin.readline

def solution():
    n, k = map(int, input().split())
    a = list(input().strip())

    cnt = 0
    for i, ai in enumerate(a):
        found = False
        if ai == 'P':
            start = 0 if i - k <= 0 else i - k
            for ti, temp in enumerate(a[start:i+1+k]):
                if found:
                    break
                if temp == 'H':
                    found = True
                    cnt += 1
                    a[start+ti] = '0'
    print(cnt)
solution()