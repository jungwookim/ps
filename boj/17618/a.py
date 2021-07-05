input = __import__('sys').stdin.readline

def solution():
    n = int(input())

    cnt = 0
    for i in range(1, n + 1):
        digits = str(i)

        sumv = sum([int(d) for d in digits])

        if i % sumv == 0:
            cnt += 1

    print(cnt)
    
solution()