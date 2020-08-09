input = __import__('sys').stdin.readline

def solution():
    n = int(input())
    a = input()[:-1]

    to_five = True
    position = 0
    multi = False

    for ai in a:
        if ai == 'P':
            to_five = not to_five
            if position == 1:
                multi = True
        else:
            position += 1
            if position == 2:
                if multi:
                    return 6
                if to_five:
                    return 5
                return 1
    else:
        return 0

print(solution())