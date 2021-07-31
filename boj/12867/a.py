input = __import__('sys').stdin.readline
from copy import deepcopy

def solution():
    n = int(input())
    m = int(input())
    a = list(map(int, input().split()))
    sign = list(input().strip())

    # n차원이지만 실제 최대는 m은 50까지 밖에 안되어서 disinct(m)차원으로 낮추어서 생각해도 무방할 것 같음
    distinct_a = list(set(a))
    line = [0 for _ in range(len(distinct_a))]
    candidates = [[0] * len(distinct_a)]

    for ai, si in zip(a, sign):
        i = distinct_a.index(ai)
        if si == '+':
            line[i] += 1
        else:
            line[i] -= 1
        candidates.append(deepcopy(line))

    for c in candidates:
        if candidates.count(c) > 1:
            print(0)
            break
    else:
        print(1)

    
solution()
