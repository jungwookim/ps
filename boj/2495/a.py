input = __import__('sys').stdin.readline
import sys
def solution():
    s = input()
    if s == '':
        sys.exit()
    ans = 1
    temp_ans = 1
    target = s[0]
    for si in s[1:]:
        if si == target:
            temp_ans += 1
        else:
            target = si
            ans = max(temp_ans, ans)
            temp_ans = 1
    else:
        ans = max(temp_ans, ans)

    print(ans)

while 1:
    solution()
