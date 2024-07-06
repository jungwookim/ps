input = __import__('sys').stdin.readline

def solution():
    while True:
        nums = list(map(int, input().split()))
        k = nums[0]

        if k == 0:
            break
        rest = nums[1:]

        used = [False] * 50

        def backtrack(start: int, seq: list):
            if len(seq) == 6:
                print(*seq)
                return

            for i in range(start, len(rest)):
                backtrack(i+1, seq + [rest[i]])
        
        backtrack(0, [])
        print()

solution()