def solution():
    s = input()

    stack = []

    ans = 0
    for i, si in enumerate(s):
        if si == "(":
            stack.append("(")
        else:
            stack.pop()
            if s[i-1] == "(":
                ans += len(stack)
            else:
                ans += 1 
    print(ans)
solution()