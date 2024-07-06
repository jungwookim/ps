input = __import__('sys').stdin.readline
import sys
sys.setrecursionlimit(10**5)

def solution():
    n, r, q = map(int, input().split())
    connect = [[] for _ in range(n+1)]
    for _ in range(n-1):
        u, v = map(int, input().split())
        connect[u].append(v)
        connect[v].append(u)


    trees = [[] for _ in range(n+1)]
    def make_tree(current_node: int, parent: int):
        for node in connect[current_node]:
            if node != parent:
                trees[current_node].append(node)
                make_tree(node, current_node)

    size = [0 for _ in range(n+1)]
    def count_subtree_nodes(current_node: int):
        size[current_node] = 1
        for node in trees[current_node]:
            count_subtree_nodes(node)
            size[current_node] += size[node]

    make_tree(r, -1)
    count_subtree_nodes(r)

    for _ in range(q):
        x = int(input())
        print(size[x], end="\n")
    

solution()