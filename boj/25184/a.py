input = __import__('sys').stdin.readline
import math
def solution():
    n = int(input())
    a = [i + 1 for i in range(n)]
    visited = [False for _ in range(n)]

    d = math.floor(n / 2)
    
    ans = []
    for i, _ in enumerate(a):
        if i + d >= n:
            break
        pair = []
        if not visited[i]:
            pair.append(a[i])
            visited[i] = True
        if not visited[i+d]:
            pair.append(a[i+d])
            visited[i+d] = True

        ans.append(pair)
    ans.reverse()
    result = []
    for e1 in ans:
        for e2 in e1:
            result.append(e2)

    print(*result)

solution()
