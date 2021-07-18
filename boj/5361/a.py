input = __import__('sys').stdin.readline

a =	350.34
b =	230.90
c = 190.55
d = 125.30
e = 180.90

def calc(*args):
    result = args[0] * a + args[1] * b + args[2] * c + args[3] * d + args[4] * e
    return "$" + f"{result:.2f}"

n = int(input())
for _ in range(n):
    l = list(map(int, input().split()))
    print(calc(*l))

