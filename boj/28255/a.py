input = __import__('sys').stdin.readline
import math

def check1(s, s1):
    return s1 + s1[::-1] + s1 == s

def check2(s, s1):
    return s1 + s1[::-1][1:] + s1[1:] == s

def check3(s, s1):
    return s1 + s1[::-1][1:] + s1 == s or s1 + s1[::-1] + s1[1:] == s


def output(result):
    if result:
        print(1)
    else:
        print(0)

def solution():
    n = int(input())

    for _ in range(n):
        s = input().strip()

        size = math.ceil(len(s) / 3)

        s1 = s[0:size]

        if len(s) % 3 == 0:
            output(check1(s, s1))
        
        if len(s) % 3 == 1:
            output(check2(s, s1))

        if len(s) % 3 == 2:
            output(check3(s, s1))

solution()