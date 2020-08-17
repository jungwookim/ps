input = __import__('sys').stdin.readline

def solution():
    n = int(input())
    e = int(input())
    
    used = [set() for _ in range(n + 1)]
    cnt = 0
    for _ in range(e):
        _, *people = map(int, input().split())
        if 1 in people:
            cnt += 1
            for p in people:
                used[p] = used[p].union(set([cnt]))
        else:
            group_sync = set()
            for p in people:
                group_sync = group_sync.union(used[p])
            for p in people:
                used[p] = group_sync

    for i, history in enumerate(used):
        if len(history) == cnt:
            print(i)

solution()