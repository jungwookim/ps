input = __import__('sys').stdin.readline

p = [0 for _ in range(105)]
p[1:11] = [1,1,1,2,2,3,4,5,7,9]

for i in range(11, 101):
    p[i] = p[i-1] + p[i-5]

def solution():
    n = int(input())
    print(p[n])

for _ in range(int(input())):
    solution()
