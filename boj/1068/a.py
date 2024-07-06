input = __import__('sys').stdin.readline

def solution():
    # 1. 이진트리를 구성한다
    # 2. 부모가 가진 자식도 지운다
    # 3. 제거 노드의 자식 노드를 연쇄적으로 다 지운다
    # 4. 리프를 수를 계산한다

    n = int(input())
    a = list(map(int, input().split()))
    m = int(input())

    v = [[] for _ in range(n)]

    for i, ai in enumerate(a):
        if ai == -1:
            continue
        v[ai].append(i)


    def del_leaf(m):
        child = v[m]
        if child == False:
            return
        
        for vi in v:
            if vi != False:
                if m in vi:
                    vi.remove(m)
        if child:
            while child:
                del_leaf(child.pop())
                v[m] = False
        else:
            v[m] = False

    del_leaf(m)
    ans = 0
    for vi in v:
        if vi != False and len(vi) == 0:
            ans += 1

    print(ans)

solution()
