from collections import deque
def solution():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    queue = deque()

    for i, ai in enumerate(a):
        queue.append({'index': i, 'value': ai})

    
    ans = 0
    while True:
        item = queue.popleft()
        max_v = max([i['value'] for i in queue])

        if item['value'] < max_v:
            queue.append(item)
        else:
            ans += 1
            if item['index'] == m:
                print(ans)
                return
        
    
solution()