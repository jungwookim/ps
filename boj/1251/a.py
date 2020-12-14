input = __import__('sys').stdin.readline

def solution():
    s = input().strip()
    size = len(s)

    arr = []
    for i in range(size):
        for j in range(size):
            w1 = s[:i]
            w2 = s[i:j]
            w3 = s[j:]
            if len(w1) == 0 or len(w2) == 0 or len(w3) == 0:
                continue
            else:
                arr.append(w1[::-1] + w2[::-1] + w3[::-1])

    arr.sort()
    print(arr[0])

solution()
