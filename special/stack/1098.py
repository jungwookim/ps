def solution():
    a = input()

    stack = []
    ans = ""
    def priority(op):
        if op in ["*", "/"]:
            return 2
        if op in ["+", "-"]:
            return 1
        return 0

    for ai in a:
        if ai == "(":
            stack.append(ai)
        elif ai == ")":
            while stack and stack[-1] != "(":
                ans += stack.pop()
            stack.pop()
        elif ai in ["*", "/", "+", "-"]:
            # 더 높은 연산자가 스택에 있다면 꺼내야한다.
            while stack and (priority(stack[-1]) >= priority(ai)):
                ans += stack.pop()
            stack.append(ai)
        else:
            ans += ai

    while stack:
        ans += stack.pop()
    print(ans)
solution()
