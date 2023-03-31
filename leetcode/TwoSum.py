def solution(nums, target):
    goals = {}
    for i, n in enumerate(nums):
        goal = target - n
        if goal in goals:
            return [i, goals[goal]]
        goals[n] = i

print(solution([2,7,11,15], 9))
print(solution([3,2,4], 6))
print(solution([3,3], 6))
