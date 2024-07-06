import copy
def solution():
    n = int(input())

    edges = {}
    visited = {}
    for _ in range(n):
        p, lc, rc = input().split()
        edges[p] = (lc, rc)
        visited[p] = False
    visited2 = copy.deepcopy(visited)
    visited3 = copy.deepcopy(visited)
    result = []
    def pre_order(m: str):
        if not visited[m]:
            left, right = edges[m]
            visited[m] = True
            result.append(m)
            if left != ".":
                pre_order(left)
            if right != ".":
                pre_order(right)

    pre_order("A")
    print(''.join(result))


    result = []
    def in_order(m: str):
        if not visited2[m]:
            left, right = edges[m]
            if left != ".":
                in_order(left)
            visited2[m] = True
            result.append(m)
            if right != ".":
                in_order(right)

    in_order("A")
    print(''.join(result))

    result = []
    def post_order(m: str):
        if not visited3[m]:
            left, right = edges[m]
            if left != ".":
                post_order(left)
            if right != ".":
                post_order(right)
            visited3[m] = True
            result.append(m)

    post_order("A")
    print(''.join(result))

solution()
