input = __import__('sys').stdin.readline

n = int(input())
info_list  = [tuple(map(int, input().split())) for _ in range(n)]

table = [0 for _ in range(n + 5)]
def solution(start): # start일에 시작한다고 했을 때 최대 수익
    if start >= n:
        return 0

    t_start, p_start = info_list[start]

    profit1 = 0
    if start + t_start <= n:
        # start일에 일을 할 때의 수익
        profit1 = p_start + table[start + t_start]
    # start일에 일을 안할 때 수익
    profit2 = table[start + 1]
    
    table[start] = max(profit1, profit2)
    return table[start]

for i in reversed(range(n)):
    solution(i)

print(max(table))
