import math
input = __import__('sys').stdin.readline


def solution():
    k, c, m = map(int, input().split())

    current_money = 0
    current_employee = 1
    max_time = math.ceil(m / k)

    time = 0

    while True:
        if current_money >= m:
            break

        current_money += (current_employee * k)
        time += 1
        if (current_money >= c):
            max_possible_hire_count = current_money // c
            new_time = math.ceil((m - (current_money - (c * max_possible_hire_count))) /
                                 ((current_employee + max_possible_hire_count) * k)) + time

            hire_count = max_possible_hire_count
            min_time = new_time

            if min_time <= max_time:
                current_employee += hire_count
                current_money -= (c * hire_count)
                max_time = min_time

    print(max_time)


solution()
