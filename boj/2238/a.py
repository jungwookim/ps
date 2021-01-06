input = __import__('sys').stdin.readline

def solution():
    u, n = map(int, input().split())

    used_arr = [0 for _ in range(u + 1)]
    name_arr = ['' for _ in range(u + 1)]

    for _ in range(n):
        name, value = input().split()
        value = int(value)

        used_arr[value] += 1
        if name_arr[value] == '':
              name_arr[value] = name

    minv = 100005

    for e in used_arr:
        if e != 0 and minv > e:
            minv = e

    for i, e in enumerate(used_arr):
        if minv == e:
            print(name_arr[i], i)
            return


solution()
