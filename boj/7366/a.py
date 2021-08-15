input = __import__('sys').stdin.readline

def solution(cid):
    n = int(input())
    a = input().strip().split()

    print("Case {}: This list contains {} sheep.".format(cid+1, a.count('sheep')))
    print()

for i in range(int(input())):
    solution(i)