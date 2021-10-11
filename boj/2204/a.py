input = __import__('sys').stdin.readline
import sys

def solution():
    n = int(input())
    if n == 0:
        sys.exit()

    ans = input().strip()
    a = ans.lower()
    for _ in range(n-1):
        temp = input().strip()
        if a > temp.lower():
            ans = temp
            a = temp.lower()

    print(ans)

while 1:
    solution()