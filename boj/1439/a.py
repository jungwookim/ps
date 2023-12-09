input = __import__('sys').stdin.readline

def solution():
    s = input().strip()
    res = [1, 0]
    init = s[0]
    idx = 0
    for char in s[1:]:
        if char != init:
            idx = 1 if idx == 0 else 0
            res[idx] += 1
            init = char
    print(min(res))
solution()
