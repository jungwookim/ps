n = int(input())

players = [[0 for _  in range(3)] for _ in range(n)]
dupls = [[] for _ in range(3)]
for i in range(n):
    r1, r2, r3 = map(int, input().split())
    if r1 in [p[0] for p in players]:
        dupls[0].append(r1)
    if r2 in [p[1] for p in players]:
        dupls[1].append(r2)
    if r3 in [p[2] for p in players]:
        dupls[2].append(r3)
    players[i][0] += r1
    players[i][1] += r2
    players[i][2] += r3

for p in players:
    sum = 0
    for i, pi in enumerate(p):
        if pi in dupls[i]:
            pass
        else:
            sum += pi
    print(sum)