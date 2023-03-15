def solution(s):
    stack = []
    open_paren = ["{", "[", "("]
    pairs = {"{" : "}", "[" : "]", "(" : ")"}
    for char in s:
        if char in open_paren:
            stack.append(char)
        else:
            if stack and pairs[stack.pop()] == char:
                pass
            else:
                return False

    if stack:
        return False
    return True

print(solution("]"))