input = __import__('sys').stdin.readline
from collections import deque

def solution():
    n, k = map(int, input().split())
    q = deque(list(range(1, n+1)))
    while len(q) != 1:
        for _ in range(k-1):
            q.append(q.popleft())
        q.popleft() # remove

    print(q.pop())

solution()