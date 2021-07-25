input = __import__('sys').stdin.readline

def solution():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    location = [0 for _ in range(100)]
    for _ in range(m):
        l, r = map(int, input().split())
        location[l] += 1
        location[r] -= 1
    
    psum = [0 for _ in range(100)]

    for i, l in enumerate(location):
        psum[i] = psum[i-1] + l
    print(psum)
    for ai in a:
        print(psum[ai])

solution()
