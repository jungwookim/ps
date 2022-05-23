input = __import__('sys').stdin.readline

def solution():
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    a = [["x" for _ in range(10)] for _ in range(10)]
    
    for i in range(10):
        for j, cell in enumerate(list(input())):
            if cell == "o":
                for ii in range(10):
                    a[i][ii] = "o"
                for jj in range(10):
                    a[jj][j] = "o"

    ans = 100
    for i in range(10):
        for j in range(10):
            if a[i][j] == "x":
                ans = min(ans, abs(x-i)+abs(y-j))
    print(ans)
solution()
