input = __import__('sys').stdin.readline

def solution():
    n = int(input())
    color_list = [None for _ in range(10 ** 5 + 2)]
    pos_list = [[] for _ in range(n + 2)]
    for _ in range(n):
        pos, color = map(int, input().split())
        color_list[pos] = color
        pos_list[color].append(pos)

    ans = 0
    for i, color in enumerate(color_list):
        if color and pos_list[color]:
            ans += min([abs(j - i) for j in pos_list[color] if i != j])

    print(ans)    

solution()
