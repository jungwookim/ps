input = __import__('sys').stdin.readline
import sys
def solution():
    a, b, c = map(int, input().split())
    if a == 0 and b == 0 and c == 0:
        sys.exit()
    if b * (c-a) < 0:
        print('X')
        return
    
    delta = c - a
    q, r = divmod(delta, b)
    if r == 0:
        print(q + 1)
    else:
        print('X')
while 1:
    solution()