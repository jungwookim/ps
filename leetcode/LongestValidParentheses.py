def solution(s):
    stack = [-1]
    ans = 0
    for i, char in enumerate(s):
        if char == "(":
            stack.append(i)
        else:
            stack.pop()
            if stack:
                ans = max(ans, i - stack[-1])
            else:
                stack.append(i)

    return ans

print(solution("(()"))
print(solution(")()())"))
print(solution(""))
print(solution("()(()"))
