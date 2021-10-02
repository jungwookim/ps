input = __import__('sys').stdin.readline

def solution():
    n, l = map(int, input().split())
    
    num = 1
    cnt = 0
    while 1:
        if str(l) in set(str(num)):
            pass
        else:
            cnt += 1
        if cnt == n:
            break
        num += 1

    print(num)

solution()