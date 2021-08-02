input = __import__('sys').stdin.readline

def solution():
    s = input().strip()
    temp = ''
    start = False
    prev = True
    for i, si in enumerate(s):
        if si == '+':
            prev = True
            temp += si
        elif si == '-':
            prev = True
            if not start:
                temp += si
                start = True
                temp += '('
            else:
                temp += ')'
                temp += si
                temp += '('
        else:
            if prev and si == '0':
                continue
            temp += si
            prev = False
    else:
        if start:
            temp += ')'
    print(eval(temp))
solution()