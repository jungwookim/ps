input = __import__('sys').stdin.readline

def solution():
    student_count = int(input())
    students = list(map(int, input().split()))
    part_count = int(input())

    candi = []
    best_time = float('inf')
    best_member = None
    for _ in range(part_count):
        i, a, b = map(int, input().split())
        if a == -1:
            continue
        time = a * 60 + b
        if time <= 360:
            if i in students:
                candi.append(i)
                if best_time > time:
                    best_time = time
                    best_member = i
    print(best_member, len(candi))

for _ in range(int(input())):
    solution()