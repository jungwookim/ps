input = __import__('sys').stdin.readline

def solution():
    n = int(input())
    a = []
    b = []

    data = []
    for _ in range(n):
        x, y = map(str, input().strip().split())
        data.append((x, y))
    
    for x, y in data:
        if x in a:
            if y in a:
                return 0
            b.append(y)
        elif x in b:
            if y in b:
                return 0
            a.append(y)
        elif y in a:
            if x in a:
                return 0
            b.append(x)
        elif y in b:
            if x in b:
                return 0
            a.append(x)
        else:
            a.append(x)
            b.append(y)
    else:
        return 1


for c in range(int(input())):
    print('Case #{}: {}'.format(c + 1, 'Yes' if solution() else 'No'))