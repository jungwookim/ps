input = __import__('sys').stdin.readline

class Node:
    def __init__(self, p, c):
        self.p = p
        self.c = c

def solution():
    n = int(input())
    tree = [[] for _ in range(100001)]
    for _ in range(n):
        p, c = map(int, input().split())
        tree[p].append(c)

    for i in range(2, n + 1):
        