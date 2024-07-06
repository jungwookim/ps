input = __import__('sys').stdin.readline
import sys
sys.setrecursionlimit(100000)
def solution():
    k = int(input())
    op = input().split()

    used = [False for _ in range(10)]

    candidates = []

    def is_valid(seq: list):
        for i in range(len(op)):
            if op[i] == "<" and not (seq[i] < seq[i+1]):
                return False
            if op[i] == ">" and not (seq[i] > seq[i+1]):
                return False
        return True
    
    def backtrack(seq: list):
        if len(seq) == k+1:
            if is_valid(seq):
                candidates.append(''.join(map(str, seq)))
            return
        
        for num in range(10):
            if not used[num]:
                used[num] = True
                seq.append(num)
                backtrack(seq)
                seq.pop()
                used[num] = False
    
    backtrack([])
    print(max(candidates))
    print(min(candidates))

solution()
