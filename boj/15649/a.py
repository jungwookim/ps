input = __import__('sys').stdin.readline

def solution():
    n, m = map(int, input().split())

    arr = [0 for _ in range(m + 1)]
    is_used = [False for _ in range(n + 1)]

    def func(k):
        if k == m:
            print(*arr[1:])
            return

        for i in range(1, n + 1):
            if not is_used[i]:
                arr[k+1] = i
                is_used[i] = True
                func(k + 1)
                is_used[i] = False

    func(0)

solution()
