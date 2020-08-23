input = __import__('sys').stdin.readline

def solution():
    n = int(input())
    a = input().split()
    lt = ''
    ans = []
    for ai in a:
        if len(ans) == 0:
            lt = ai
            ans.append(ai)
        else:
            if ai <= lt:
                ans.insert(0, ai)
                lt = ai
            else:
                ans.append(ai)

    for e in ans:
        print(e, end='')
    print()

for _ in range(int(input())):
    solution()
