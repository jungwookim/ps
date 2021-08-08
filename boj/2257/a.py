input = __import__('sys').stdin.readline

def solution():
    c = input().strip()
    dic = {
        "H": 1,
        "C": 12,
        "O": 16
    }
    s = [[0]]

    for ci in c:
        if ci == '(':
            s.append([0])
        elif ci == ')':
            last = sum(s.pop())
            s[-1].append(last)
        elif ci in dic.keys():
            val = dic[ci]
            s[-1].append(val)
        else: # numbers
            s[-1][-1] *= int(ci)

    print(sum(s[0]))
solution()