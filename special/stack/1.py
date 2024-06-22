"""
숫자가 주어지고 m자리의 숫자를 제거해서 가장 큰 숫자를 만들라
input: 5267823 3
output: 7823

input: 9977252641 5
output: 99776
"""
def solution():
    n, m = map(int, input().split())
    n = map(int, str(n))

    stack = []
    for i in n:
        while stack and m > 0 and stack[-1] < i:
            stack.pop()
            m -= 1
        stack.append(i)

    if m != 0:
        stack = stack[:-m]

    for i in stack:
        print(i, end="")
solution()
