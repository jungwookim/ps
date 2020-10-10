input = __import__('sys').stdin.readline

def solution():
    a, b, c, d = map(int, input().split())
    
    print(min([abs((a+b) - (c+d)), abs((a+c) - (b+d)), abs((a+d) - (b+c))]))

solution()
