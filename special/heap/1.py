import heapq

def solution():
    min_heap = []

    while True:
        v = int(input())
        if v == -1:
            return
        if v == 0:
            if len(min_heap) == 0:
                print(-1)
            else:
                print(heapq.heappop(min_heap))
        else:
            heapq.heappush(min_heap, v)

solution()
