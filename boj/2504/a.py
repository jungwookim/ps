input = __import__('sys').stdin.readline

def solution():
    a = input().strip()
    s = []
    val = [0]
    for c in a:
        if c == '(':
            s.append(2)
            val.append(0)
        elif c == '[':
            s.append(3)
            val.append(0)
        elif c == ')':
            if len(s) == 0:
                print(0)
                return
            popv = val.pop()
            machedv = s.pop()
            if machedv != 2:
                print(0)
                return
            val[-1] += max(1, popv) * 2
        elif c == ']':
            if len(s) == 0:
                print(0)
                return
            popv = val.pop()
            machedv = s.pop()
            if machedv != 3:
                print(0)
                return  
            val[-1] += max(1, popv) * 3
    print(val[0])

solution()
