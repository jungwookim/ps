import sys
def prime_list(n):
    sieve = [True] * n

    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:
            for j in range(i+i, n, i):
                sieve[j] = False

    return [i for i in range(2, n) if sieve[i] == True]

primes = prime_list(2**15)

def solution():
    n = int(input())
    if n == 0:
        sys.exit()

    cnt = 0
    for p in primes:
        if n - p >= p and n - p in primes:
            cnt += 1
    print(cnt)

while 1:
    solution()
