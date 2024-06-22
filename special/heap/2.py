import heapq

def solution():
    max_heap = []

    while True:
        v = int(input())
        if v == -1:
            return
        if v == 0:
            if len(max_heap) == 0:
                print(-1)
            else:
                print(-heapq.heappop(max_heap))
        else:
            heapq.heappush(max_heap, -v)

solution()
