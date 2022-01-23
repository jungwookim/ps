input = __import__('sys').stdin.readline

n = int(input())

def solution():
    ans = []
    def hanoi(n, start, mid, to):
        if n == 1:
            ans.append([start, to])
            return

        hanoi(n - 1, start, to, mid) # n-1개를 중간으로 옮김

        ans.append([start, to]) # 1개를 목적지로 옮김

        hanoi(n - 1, mid, start, to) # 중간에 있는 녀석들을 나머지 n-1개를 목적지로 옮김
    

    hanoi(n, 1, 2, 3)

    print(len(ans))
    for ai in ans:
        print(*ai)

solution()
