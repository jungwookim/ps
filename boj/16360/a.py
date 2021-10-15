input = __import__('sys').stdin.readline

"""
-a	-as
-i, -y	-ios
-l	-les
-n, -ne	-anes
-o	-os
-r	-res
-t	-tas
-u	-us
-v	-ves
-w	-was
"""
def solution():
    n = int(input())

    for _ in range(n):
        word = input().strip()

        if word[-1] == 'a':
            print(word[:-1] + 'as')
        elif word[-1] == 'i' or word[-1] == 'y':
            print(word[:-1] + 'ios')
        elif word[-1] == 'l':
            print(word[:-1] + 'les')
        elif word[-1] == 'n':
            print(word[:-1] + 'anes')
        elif word[-2:] == 'ne':
            print(word[:-2] + 'anes')
        elif word[-1] == 'o':
            print(word[:-1] + 'os')
        elif word[-1] == 'r':
            print(word[:-1] + 'res')
        elif word[-1] == 't':
            print(word[:-1] + 'tas')
        elif word[-1] == 'u':
            print(word[:-1] + 'us')
        elif word[-1] == 'v':
            print(word[:-1] + 'ves')
        elif word[-1] == 'w':
            print(word[:-1] + 'was')
        else:
            print(word + 'us')
        
solution()