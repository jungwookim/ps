input = __import__('sys').stdin.readline

def solution():
    s = input().strip()

    alphabets = [chr(i) for i in range(ord('a'), ord('z') + 1)]
    q_list = [0, 3, 3, 3, 3, 3, 4, 3, 4]
    q_list.reverse()

    arr = [[] for _ in range(len(q_list))]
    for i, q in enumerate(q_list):
        for _ in range(q):
            arr[len(q_list) - i - 1].append(alphabets.pop())


    numbers = []
    for char in s:
        lower_char = char.lower()
        for i, e in enumerate(arr):
            if lower_char in e:
                numbers.append(i + 2)
                break

    print(sum(numbers))
solution()