input = __import__('sys').stdin.readline

def solution(cid):
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort(reverse=True)

    disks = [x for _ in range(n)]
    used_count = [0 for _ in range(n)]

    for ai in a:
        used = False
        for pointer in range(n):
            if not used:
                if disks[pointer] - ai >= 0 and used_count[pointer] < 2:
                    disks[pointer] -= ai
                    used_count[pointer] += 1
                    used = True

    ans = sum([1 for disk in disks if disk != x])
    print("Case #{}: {}".format(cid, ans))
    


for i in range(int(input())):
    solution(i+1)