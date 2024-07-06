def solution(l1, l2):
    total = int("".join(map(str, l1))) + int("".join(map(str, l2)))
    return list(str(total)[::-1])

print(solution([2,4,3], [5,6,4]))
print(solution([0], [0]))
print(solution([9,9,9,9,9,9,9], [9,9,9,9]))