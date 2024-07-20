import math
input = __import__('sys').stdin.readline

def solution():
    numbers = list(map(int, input().split()))
    for num in range(1, numbers[0]):
        numbers.append(num)
        numbers.sort(reverse=True)
        a, b, c, d = numbers
        if math.isclose(a*c + b*d, (a ** 2 - d ** 2)**0.5 * (a ** 2 - b ** 2)**0.5) or math.isclose(a*d + b*c, (a ** 2 - c ** 2)**0.5 * (a ** 2 - b ** 2)**0.5):
            return num
        numbers.remove(num)
    return -1

print(solution())