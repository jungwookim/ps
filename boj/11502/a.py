from itertools import combinations_with_replacement

primes = []

for i in range(2, 1001):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        primes.append(i)

def solution():
    n = int(input())
    
    for c in combinations_with_replacement(primes, 3):
        if n == sum(list(c)):
            print(*list(c))
            return
    else:
        print(0)
    

for _ in range(int(input())):
    solution()
