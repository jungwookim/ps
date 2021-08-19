input = __import__('sys').stdin.readline
import sys

def solution():
    a = input().strip()
    if a == '#':
        sys.exit()

    for word in a.split():
        print(word[::-1], end=' ')
    print('')

while True:
    solution()