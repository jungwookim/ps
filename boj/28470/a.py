input = __import__('sys').stdin.readline
import math
def solution():
    n = int(input())
    a = map(int, input().split())
    b = map(int, input().split())
    k = map(float, input().split())

    ans = 0
    for ai, bi, ki in zip(a, b, k):
        if ki > 1:
            ans += int(ai * (ki * 10)) // 10 - bi
        else:
            ans += ai - int(bi * (ki * 10)) // 10

    print(ans)

solution()
