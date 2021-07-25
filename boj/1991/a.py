input = __import__('sys').stdin.readline

class Node:
    def __init__(self, par, left, right):
        self.par = par
        self.left = left
        self.right = right


def solution():
    n = int(input())
    tree = []
    for _ in range(n):
        par, left, right = input().split()
        node = Node(par, left, right)
        tree.append(node)
