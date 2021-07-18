input = __import__('sys').stdin.readline

def solution():
    n = int(input())
    if n % 2 == 1:
        print('SK')
    else:
        print('CY')

solution()
