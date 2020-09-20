input = __import__('sys').stdin.readline

def solution():
    n = int(input())
    s = input().strip()
    s_list = ['' for _ in range(n)]
    for i in range(n):
        if s[i] != '?':
            s_list[-(i+1)], s_list[i] = s[i], s[i]
        elif s[-(i+1)] != '?':
            s_list[-(i+1)], s_list[i] = s[-(i+1)], s[-(i+1)]
        else:
            s_list[i], s_list[-(i+1)] = 'a', 'a'

    print(''.join(s_list))
solution()
