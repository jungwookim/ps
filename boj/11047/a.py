input = __import__('sys').stdin.readline

def solution():
    n, k = map(int, input().split())
    a = []
    for _ in range(n):
        a.append(int(input()))

    ans = 0
    while a:
        q, r = divmod(k, a.pop())
        k = r
        ans += q
        if r == 0:
            break
    
    print(ans)

solution()
