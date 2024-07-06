def solution(nums):
    n = len(nums)
    
    for num in nums:
        index = abs(num) - 1
        nums[index] = -abs(nums[index])

        print(nums)
    
    missing_numbers = [i + 1 for i in range(n) if nums[i] > 0]
    
    return missing_numbers

print(solution([4,3,2,7,8,2,3,1]))

"""
추가 공간을 사용하지 않고 풀기 위해서 nums를 바로 갱신하도록 해야한다.
num의 index에 해당 하는 값을 음수로 만들고
양수로 남아있는 값을 출력한다.
[4, 3, 2, -7, 8, 2, 3, 1]
[4, 3, -2, -7, 8, 2, 3, 1]
[4, -3, -2, -7, 8, 2, 3, 1]
[4, -3, -2, -7, 8, 2, -3, 1]
[4, -3, -2, -7, 8, 2, -3, -1]
[4, -3, -2, -7, 8, 2, -3, -1]
[4, -3, -2, -7, 8, 2, -3, -1]
[-4, -3, -2, -7, 8, 2, -3, -1]
"""