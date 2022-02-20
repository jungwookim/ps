input = __import__('sys').stdin.readline
from collections import deque
def solution():
    n = int(input())
    l = deque([1 for _ in range(13)])
    r = deque([1 for _ in range(14)])
    l[0] = 0
    joker_position = []

    new = deque([])
    for _ in range(n):
        a = list(map(int, input().split()))
        for i, ai in enumerate(a):
            if i % 2 == 0:
                for _ in range(ai):
                    new.append(r.popleft())
            else:
                for _ in range(ai):
                    new.append(l.popleft())

        l = deque(list(new)[:13])
        r = deque(list(new)[13:])

        for i, ni in enumerate(new):
            if ni == 0:
                joker_position.append(i+1)
        new = deque([])
    print(joker_position[-1])
solution()
