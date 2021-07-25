input = __import__('sys').stdin.readline

def solution():
    s = 'quack'
    a = input().strip()
    arr = [[] for _ in range(len(a) // 5)]

    candi = []
    for char in a:
        for i in range(len(arr)):
            print(arr)
            if len(arr[i]) != 0:
                if char == 'q':
                    continue
                if arr[i][-1] == char:
                    continue
                else:
                    if s[s.index(char)-1] == arr[i][-1]:
                        arr[i].append(char)
                        break
                    else:
                        continue
            else:
                arr[i].append(char)
                break
        else:
            print(-1)
            return
        for i in range(len(arr)):
            cnt = sum([1 for ai in arr[i] if len(ai) > 0])
            sub = sum([1 for ai in arr[i] if len(ai) == 5])
            candi.append(cnt - sub)
    print(candi)
    print(min(candi))
for _ in range(int(input())):
    solution()
