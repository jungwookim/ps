input = __import__('sys').stdin.readline
import math
def solution():
    n, m, k = map(int, input().split())
    max_game = math.log2(n)
    print(int(min(math.floor(math.log2(k)) + m, max_game)))

solution()