input = __import__('sys').stdin.readline
import sys
def solution():
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        sys.exit()

    m = [[0 for _ in range(w + 2)]] + [[0] + list(map(int, input().split())) + [0] for _ in range(h)] + [[0 for _ in range(w + 2)]]
    def search(x, y):
        if m[x][y] == 0:
            return
        
        m[x][y] = 0
        search(x+1, y)
        search(x+1, y+1)
        search(x, y+1)
        search(x-1, y+1)
        search(x-1, y)
        search(x-1, y-1)
        search(x, y-1)
        search(x+1, y-1)

    cnt = 0
    for i in range(1, h+1):
        for j in range(1, w+1):
            if m[i][j] == 1:
                search(i, j)
                cnt += 1
    print(cnt)
while True:
    solution()