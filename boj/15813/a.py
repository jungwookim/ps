input = __import__('sys').stdin.readline

def solution():
    n = int(input())
    name = input().strip()

    dic = {}
    for j, i in enumerate(range(ord('A'), ord('Z') + 1)):
        dic[chr(i)] =  j + 1

    print(sum([dic[char] for char in name]))

solution()
