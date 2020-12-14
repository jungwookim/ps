from collections import deque  

def solution():
    n = int(input())
    
    queue = deque([])
    cow_num = 1
    for _ in range(n):
        inputs = list(input().split())
        a = inputs[0]
        b = inputs[1]
        if a == 'A':
            if b == 'L':
                queue.appendleft(cow_num)
            else:
                queue.append(cow_num)
            cow_num += 1
        elif a == 'D':
            c = inputs[2]
            if b == 'L':
                for _ in range(int(c)):
                    queue.popleft()
            else:
                for _ in range(int(c)):
                    queue.pop()

    for cow in queue:
        print(cow)

solution()
