input = __import__('sys').stdin.readline

def solution():
    inputs = []
    while 1:
        si = input().strip()
        if si == '':
            break
        inputs.append(si)
    s = ''.join(inputs)
    print(sum(map(int, s.split(','))))

solution()
