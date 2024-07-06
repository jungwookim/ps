def solution(s):
    l = 0
    r = 0
    
    result = 1
    cur = set()
    cur.add(s[0])
    while True:
        r += 1
        print("cur", cur)
        print("result", result)
        if len(s) == r:
            break
        if s[r] in cur:
            # same result
            # remove target and inc l
            cur.remove(s[r])
            l += 1
        else:
            # inc result
            result += 1
            # add cur
            cur.add(s[r])
    return result

print(solution("abcabcbb"))
print(solution("bbbbb"))
print(solution("pwwkew"))
