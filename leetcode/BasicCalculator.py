def solution(s):
    cur, res, sign, stack = 0, 0, 1, []

    for char in s:
        if char.isdigit():
            cur = cur * 10 + int(char)
        elif char in ["+", "-"]:
            res += cur * sign
            if char == "+":
                sign = 1
            else:
                sign = -1
            cur = 0
        elif char == "(":
            stack.append(res)
            stack.append(sign)
            sign = 1
            res = 0
        elif char == ")":
            res += (sign * cur)
            res *= stack.pop()
            res += stack.pop()
            cur = 0
    
    return res + sign * cur
