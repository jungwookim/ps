input = __import__('sys').stdin.readline

def solution():
    n, m = map(int, input().split())

    dic = {}
    for _ in range(n):
        word = input().strip()

        if len(word) < m:
            continue
        
        if word in dic:
            dic[word] += 1
        else:
            dic[word] = 1

    for ans in list(map(lambda x: x[0], sorted(dic.items(), key=lambda x: (-x[1], -len(x[0]), x[0])))):
        print(ans)

solution()