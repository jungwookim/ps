input = __import__('sys').stdin.readline

def solution():
    n, p = map(int, input().split())
    if n == 1:
        print("9 3")
        return
    str_p = str(p)
    list_p = list(map(int, str_p))
    sum_digits = sum(list_p)
    r = sum_digits % 3
    result = []
    for i in range(n):
        temp_list = list(map(int, str_p))
        temp_list[i] = temp_list[i] - r if temp_list[i] - r > 0 else temp_list[i] - r + 3
        result.append(temp_list)

    for r in result:
        print("".join(map(str, r)), 3)

for _ in range(int(input())):
    solution()