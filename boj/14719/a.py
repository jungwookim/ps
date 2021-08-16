input = __import__('sys').stdin.readline

def solution():
    h, w = map(int, input().split())
    w_list = list(map(int, input().split())) # length w

    ans = 0
    for hi in range(1, h+1):
        cnt = 0
        height = 0
        for wi in w_list:
            if hi <= wi:
                ans += cnt
                height = hi
                cnt = 0
                continue

            if height == hi:
                cnt += 1

    print(ans)
        
solution()