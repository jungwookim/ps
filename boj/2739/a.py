input = __import__('sys').stdin.readline

def solution():
    n = int(input())
    
    for i in range(1, 10):
        print('{} * {} = {}'.format(n, i, n*i))

solution()