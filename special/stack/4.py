def solution():
    a = input()

    stack = []
    if len(a) == 1:
        print(a)
        return
    
    for ai in a:
        if ai.isnumeric():
            stack.append(ai)
        else:
            y = stack.pop()
            x = stack.pop()
            if ai == "*":
                temp = int(x) * int(y)
            elif ai == "/":
                temp = int(x) / int(y)
            elif ai == "+":
                temp = int(x) + int(y)
            else:
                temp = int(x) - int(y)
                
            stack.append(temp)

    print(temp)

solution()
