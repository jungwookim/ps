input = __import__('sys').stdin.readline

def solution():
    n = int(input())
    a = list(map(int, input().split()))
    goal = sorted(a)
    ans = []

    def process(arr):
        i = 0
        ans = 0

        while i < n-1:
            lv = arr[i]
            rv = arr[i+1]

            if lv > rv:
                arr[i] = rv
                arr[i+1] = lv
                return arr, i+1, i+2

            else:
                i += 1
    
    if n == 1 or a == goal:
        print(0)
        return
    
    while True:
        a, l, r = process(a)
        ans.append((l, r))
        if a == goal:
            break
    
    if len(ans) > 100:
        print(-1)
    else:
        print(len(ans))
        for e in ans:
            print(*e)
solution()
