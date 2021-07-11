import sys

def solution(g):
    n = int(input())
    if n == 0:
        sys.exit()
    print("Group {}".format(g))
    temp = [[] for _ in range(n)]
    names = []
    for i in range(n):
        a, *l = list(map(str, input().split()))
        for j, lj in enumerate(l):
            if lj == 'N':
                temp[i].append(j + 1)
        names.append(a)
    is_someone = False
    for i, ti in enumerate(temp):
        if len(ti) != 0:
            for j in ti:
                is_someone = True
                print("{} was nasty about {}".format(names[i-j], names[i]))
        
        
    if not is_someone:
        print("Nobody was nasty")
        

    print('')

group = 0
while True:
    group += 1
    solution(group)