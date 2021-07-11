def solution():
    m = int(input())
    a = [0]
    current_sum = 0
    current_xor = 0
    for _ in range(m):
        inp = list(input().strip().split())
        if int(inp[0]) == 1:
            current_sum += int(inp[1])
            current_xor ^= int(inp[1])
            continue
        if int(inp[0]) == 2:
            current_sum -= int(inp[1])
            current_xor ^= int(inp[1])
            continue
        if int(inp[0]) == 3:
            print(current_sum)
            continue
        if int(inp[0]) == 4:
            print(current_xor)
            continue
        

solution()