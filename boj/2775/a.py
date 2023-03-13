input = __import__('sys').stdin.readline
a = [[0 for _ in range(15)] for _ in range(15)]
for ni in range(15):
    a[0][ni] = ni


for i in range(1, 15):
    for j in range(1, 15):
        a[i][j] = sum([a[i-1][jj] for jj in range(1, j + 1)])

def solution():    
    k = int(input())
    n = int(input())
    print(a[k][n])

for _ in range(int(input())):
    solution()
