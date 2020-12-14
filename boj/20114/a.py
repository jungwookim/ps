input = __import__('sys').stdin.readline

def solution():
    n, h, w = map(int, input().split())

    ans = ['?' for _ in range(n)]
    for _ in range(h):
        a = input().strip()
        for j, i in enumerate(range(0, n * w, w)):
            sub_set = set(a[i : i + w])
            if len(sub_set) > 1:
                sub_set.remove('?')
            if ans[j] == '?':
                ans[j] = list(sub_set)[0]


    print(''.join(ans))

solution()
