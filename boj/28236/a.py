input = __import__('sys').stdin.readline

def solution():
    n, m, k = map(int, input().split())

    goal_x = m-1

    ans = k
    distance = n + m
    for i in range(1, k + 1):
        floor, section = map(int, input().split())
        x = section - 1
        y = floor - 1

        if y + goal_x - x < distance:
            distance = y + goal_x - x
            ans = i
    print(ans)
    return ans

solution()
