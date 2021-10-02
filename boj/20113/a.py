input = __import__('sys').stdin.readline

def solution():
    n = int(input())
    a = list(map(int, input().split()))
    
    vote = [0 for _ in range(n+1)]

    for ai in a:
        vote[ai] += 1

    max_count = max(vote)

    max_index = [i for i, c in enumerate(vote) if c == max_count]

    if len(max_index) == 1 and max_index[0] >= 1:
        print(max_index[0])
    elif len(max_index) == 2:
        if 0 in max_index:
            print(max_index[1])
        else:
            print('skipped')
    else:
        print('skipped')

solution()