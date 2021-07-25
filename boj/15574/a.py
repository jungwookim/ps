input = __import__('sys').stdin.readline

def solution():
    n = int(input())
    a = [list(map(int, input().split())) for _  in range(n)]
    tmp = [[] for _ in range(n + 5)]
    _key = a[0][0]
    key = [0 for _ in range(n + 5)]
    a.sort(key=lambda x: (x[0], x[1]))
    i = 0
    for x, y in a:
        if x == _key:
            pass
        else:
            _key = x
            i += 1
        tmp[i].append(y)
        key[i] = _key
        
solution()