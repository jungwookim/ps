input = __import__('sys').stdin.readline

def solution():
    n = int(input())
    s = input().strip()
    ss = s
    def calc(a):
        left = []
        right = []
        for i in range(0, len(a), 2):
            temp = a[i:i+3]
            if len(temp) == 0:
                continue
            elif len(temp) == 1:
                left.append(temp[0])
            else:
                left.append(temp[0])
                right.append(temp[1])
        while len(right) > 0:
            left.append(right.pop())
        return ''.join(left)
    
    i = 1
    repeat = 1
    while i <= n:
        s = calc(s)
        if s == ss:
            repeat = i
            break
        i += 1

    n = n % repeat
    j = 1
    while j <= n:
        s = calc(s)
        j += 1
    print(s)

solution()