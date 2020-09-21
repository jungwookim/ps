input = __import__('sys').stdin.readline

def solution():
    string = input().strip().split(',')
    print(len(string))
solution()