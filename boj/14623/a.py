a = input()
b = input()

a = int(a, 2)
arr = []
size = len(b) - 1
for i, char in enumerate(b):
    multiplier = size - i
    if char == '1':
      arr.append(a << multiplier)

print("{0:b}".format(sum(arr)))
