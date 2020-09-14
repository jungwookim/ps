input = __import__('sys').stdin.readline

def solution():
    s = input().strip()
    temp_list = list()
    result_list = list()

    for char in s:
        if char == '-':
            if len(result_list) != 0:
                result_list.pop()
        elif char == '<':
            if len(result_list) != 0:
                temp_list.append(result_list.pop())
        elif char == '>':
            if len(temp_list) != 0:
                result_list.append(temp_list.pop())
        else:
            result_list.append(char)

    temp_list.reverse()
    ans1 = ''.join(result_list)
    ans2 = ''.join(temp_list)
    print(ans1 + ans2)

for _ in range(int(input())):
    solution()
