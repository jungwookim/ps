input = __import__('sys').stdin.readline

def solution():
    a, b, c = map(int, input().split())

    A = dict()
    B = dict()
    C = dict()
    for _ in range(a):
        menu, price = input().split()
        A[menu] = int(price)
    for _ in range(b):
        menu, price = input().split()
        B[menu] = int(price)
    for _ in range(c):
        menu = input().strip()
        C[menu] = True
    
    cost = 0
    
    left_B = []
    left_C = []
    for _ in range(int(input())):
        menu = input().strip()
        if menu in A:
            cost += A[menu]
        elif menu in B:
            left_B.append(menu)
        else:
            left_C.append(menu)

    for menu_b in left_B:
        if cost >= 20000:
            cost += B[menu_b]
        else:
            return 'No'

    used = False

    for menu_c in left_C:
        if used:
            return 'No'
        if cost >= 50000:
            used = True
            continue
        else:
            return 'No'

    return 'Okay'

print(solution())