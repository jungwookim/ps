input = __import__('sys').stdin.readline
import heapq

def solution():
    n = int(input())

    heap = []
    for _ in range(n):
        a = int(input())

        if a == 0:
            if len(heap) == 0:
                print(0)
            else:
                print(heapq.heappop(heap))
        else:
            heapq.heappush(heap, a)

solution()
        