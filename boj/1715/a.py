input = __import__('sys').stdin.readline
import heapq

def solution():
    n = int(input())
    q = []

    ans = 0
    for _ in range(n):
        heapq.heappush(q, int(input()))
    a = 0
    b = 0
    while len(q) > 1:
        a = heapq.heappop(q)
        b = heapq.heappop(q)
        ans += (a + b)
        heapq.heappush(q, a + b)
    print(ans)

solution()
