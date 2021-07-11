def solution():
    n, m = map(int, input().split())
    dic = {}
    for _ in range(n):
        team = input()
        member_count = int(input())
        members = [input() for _ in range(member_count)]
        dic[team] = members

    for _ in range(m):
        q = input()
        t = int(input())
        if t == 1:
            for t, m in dic.items():
                if q in m:
                    print(t)
        else:
            for t, m in dic.items():
                if t == q:
                    for n in sorted(m):
                        print(n)

solution()