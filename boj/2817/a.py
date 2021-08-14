input = __import__('sys').stdin.readline

def solution():
    x = int(input())
    n = int(input())

    a = []
    names = set()
    for _ in range(n):
        name, vote = input().strip().split()
        vote = int(vote)

        if vote / x < 0.05:
            continue
        else:
            for i in range(1, 15):
                a.append([name, vote / i])
                names.add(name)

    sorted_a = sorted(a, key=lambda x : (-x[1], x[0]))

    final = sorted_a[:14]

    ans_dic = {x:0 for x in names}
    for a, b in final:
        ans_dic[a] += 1
    for res in sorted(ans_dic.items(), key=lambda x: (x[0])):
        print(*res)

solution()