input = __import__('sys').stdin.readline

def solution():
    n = int(input())
    a = list(map(int, input().split()))

    b = {}

    # { value: index }
    for i, ai in enumerate(a):
        b[ai] = i

    ans = 1
    lt = b[1]
    rt = b[1]
    for i in range(1, 1 + n):
        if i == 1:
            continue
        else:
            target = b[i]
            if lt >= target:
                lt = target

            if rt <= target:
                rt = target
            
            if rt - lt < i:
                ans += 1
    print(ans)

solution()
