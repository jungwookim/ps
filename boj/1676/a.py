input = __import__('sys').stdin.readline

def solution():
    n = int(input())

    def f(x):
        c2 = 0
        c5 = 0
        while x % 2 == 0:
            if x % 2 == 0:
                c2 += 1
                x //= 2


        while x % 5 == 0:
                if x % 5 == 0:
                    c5 += 1
                    x //= 5
        return c2, c5

    count2 = 0
    count5 = 0
    for i in range(1, n+1):
        c1, c2 = f(i)
        count2 += c1
        count5 += c2

        
    print(min(count2, count5))

solution()        