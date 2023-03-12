def solution():
    s = input().strip()
    s1 = s.split("-")
    ans = []
    for si in s1:
        s2 = si.split("+")
        ans.append(sum(map(int, s2)))
    res = 0
    for i in range(len(ans)):
        if i == 0:
            res += ans[i]
        else:
            res -= ans[i] 
    print(res)

solution()
