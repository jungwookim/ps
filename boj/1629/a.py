input = __import__('sys').stdin.readline

def solution():
    a, b, c = map(int, input().split())

    def pow(x, y, m):
        if y == 0:
            return 1
        
        half = pow(x, y // 2, m)
        res = (half * half) % m

        if y % 2 == 0:
            return res
        else:
            return (res * x) % m

    print(pow(a, b, c))

solution()
