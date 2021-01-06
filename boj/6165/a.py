input = __import__('sys').stdin.readline

def solution():
    n = int(input())

    sets = set()
    dots = []
    for _ in range(n):
        dots.append(list(map(int, input().split())))

    for i in range(n):
        for j in range(i + 1, n):
            if i != j:
              p1 = dots[i]
              p2 = dots[j]
            
              slope = (p2[1] - p1[1]) / (p2[0] - p1[0]) if p2[0] != p1[0] else 'inf'

              sets.add(slope)


    print(len(sets))

solution()
