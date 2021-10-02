input = __import__('sys').stdin.readline

def solution():
    n = int(input())
    a = list(input().strip())

    count_list = [[0, 0] for _ in range(len(a) + 1)]
    
    for i in range(1, len(a)+1):
        if a[i-1] == 'M':
            count_list[i][0] += count_list[i-1][0] + 1
            count_list[i][1] += count_list[i-1][1]
        else:
            count_list[i][0] += count_list[i-1][0]
            count_list[i][1] += count_list[i-1][1] + 1

    diff = list(map(lambda x : abs(x[0] - x[1]), count_list))

    seen = 0
    ans = 0
    for i, d in enumerate(diff):
        if seen >= 2:
            break
        if d <= n:
            seen = 0
            ans = max(sum(count_list[i]), ans)
        else:
            seen += 1

    print(ans)

solution()