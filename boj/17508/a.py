def find_symm(card):
    if card == '6':
        return '9'
    if card == '9':
        return '6'
    if card == '7':
        return '-7'
    if card == '-7':
        return '7'
    return '8'

def solution():
    n, m = map(int, input().split())
    matrix = [list(input()) for _ in range(n)]

    ans = 0
    for i in range(n):
        for j in range(m):
            cur = matrix[i][j]
            oppo = matrix[n - 1 - i][m - 1 - j]

            target = find_symm(cur)

            if i == n - 1 - i and j == m - 1 - j:
                if cur in ['6', '9', '7']:
                    print(-1)
                    return

            if oppo == target:
                pass
            else:
                if oppo != cur:
                    print(-1)
                    return
                matrix[n - 1 - i][m - 1 - j] = target
                ans += 1

    print(ans)

solution()