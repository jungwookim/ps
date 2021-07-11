# Equilateral, Isosceles, Scalene, Invalid
import sys

def solution():
    a = list(map(int, input().split()))
    if a[0] == 0:
        sys.exit()
    
    largest = max(a)
    if (sum(a) - largest) <= largest:
        print('Invalid')
        return
    if len(set(a)) == 2:
        print('Isosceles')
        return
    if len(set(a)) == 1:
        print('Equilateral')
        return
    print('Scalene')

while 1:
    solution()