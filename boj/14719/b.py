input = __import__('sys').stdin.readline

def solution():
    h, w = map(int, input().split())
    a = list(map(int, input().split())) # length w

    used = [False for _ in range(w)]
    ans = 0

    def calc(v, arr, used):
        ans = 0
        if len(arr) <= 1:
            return ans
        for i in range(len(arr)):
            if i == len(arr)-1:
                break
            for j, wj in enumerate(a[arr[i]+1:arr[i+1]]):
                if not used[arr[i]+j]:
                    ans += max(v - wj, 0)
                    used[arr[i]+j] = True
        return ans

    for hi in reversed(range(0, h+1)):
        above_index = []
        for i, wi in enumerate(a):
            if hi <= wi:
                above_index.append(i)

        ans += calc(hi, above_index, used)

    print(ans)
        
solution()