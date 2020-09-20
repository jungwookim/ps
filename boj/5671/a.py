input = __import__('sys').stdin.readline

def check_dupicate(number):
    number = str(number)
    for i, cur_digit in enumerate(number):
        for digit in number[i+1:]:
            if cur_digit != digit:
                pass
            else:
                return True
    return False

    
def solution():
    inp = list(map(int, input().split()))
    if len(inp) == 0:
        return 'STOP'
    n, m = inp
    ans = 0
    for i in range(n, m + 1):
        if not check_dupicate(i):
            ans += 1

    print(ans)

while 1:
    result = solution()
    if result == 'STOP':
        break
