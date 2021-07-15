input = __import__('sys').stdin.readline

def converter(x, unit):
    if unit == 'kg':
        return kg_to_pound(x)
    if unit == 'l':
        return liter_to_gallon(x)
    if unit == 'lb':
        return pound_to_kg(x)
    if unit == 'g':
        return gallon_to_liter(x)

def formatter(n):
    return f'{n:.4f}'

def kg_to_pound(x):
    return formatter(2.2046 * x), 'lb'

def pound_to_kg(x):
    return formatter(0.4536 * x), 'kg'

def liter_to_gallon(x):
    return formatter(0.2642 * x), 'g'

def gallon_to_liter(x):
    return formatter(3.7854 * x), 'l'

def solution():
    n = int(input())
    for _ in range(n):
        x, unit = input().split()
        x = float(x)
        print(*converter(x, unit))


solution()