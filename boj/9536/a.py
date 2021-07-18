input = __import__('sys').stdin.readline

def solution():
    sounds = list(map(str, input().split()))


    while 1:
        l = list(map(str, input().split()))
        if len(l) == 5:
            print(*sounds)
            break
        sounds = [sound for sound in sounds if sound != l[2]]

for _ in range(int(input())):
    solution()