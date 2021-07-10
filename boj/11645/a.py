input = __import__('sys').stdin.readline

def solve():
    n = int(input())
    print(len(set([input().strip() for _ in range(n)])))

for _ in range(int(input())):
    solve()