input = __import__('sys').stdin.readline

def solution():
    n, m = map(int, input().split())
    matrix = []

    def calc(target):
        cnt1 = 0
        cnt2 = 0
        for i in range(8):
            for j in range(8):
                if (i + j) % 2 == 1:
                    if target[i][j] == 'W':
                        cnt1 += 1
                    else:
                        cnt2 += 1
                else:
                    if target[i][j] == 'B':
                        cnt1 += 1
                    else:
                        cnt2 += 1

        return min(cnt1, cnt2)

    for _ in range(n):
        matrix.append(list(input().strip()))

    ans = float("inf")
    for i in range(n):
        for j in range(m):
            rows = matrix[i:i+8]
            temp_map = [row[j:j+8] for row in rows]
            if len(rows) != 8 or len(rows) != 0 and len(temp_map[0]) != 8:
                continue
            
            result = calc(temp_map)
            if ans > result:
                ans = result

    print(ans)

solution()