input = __import__('sys').stdin.readline

max_size = 10**6
arr = list(range(1, max_size + 1));
root_max_size = int(max_size ** 0.5)

a = [[] for _ in range(root_max_size)]
for i in arr:
    idx = i % root_max_size
    if idx == 0:
        idx = root_max_size
    a[idx-1].append(i)

for ai in a:
    ai.reverse()

flat_a = []

for sub_a in a:
    for ai in sub_a:
        flat_a.append(ai)
print(*flat_a)

