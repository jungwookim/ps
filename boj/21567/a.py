input = __import__('sys').stdin.readline

a = int(input())
b = int(input())
c = int(input())
for i in range(10):
    print(str(a*b*c).count(str(i)))