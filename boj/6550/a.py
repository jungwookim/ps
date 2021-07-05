import sys
def solution():
    try:
        s, t = input().strip().split()
        if len(s) > len(t):
            print('No')
            return

        current_index = 0
        for si in s:
            target_index = t[current_index:].find(si)
            if target_index != -1:
                current_index = target_index + current_index + 1
            else:
                print('No')
                return
        else:
            print('Yes')
    except:
        sys.exit()

while 1:
    solution()
