from typing import List

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        size = len(nums)
        s = [0]
        for i in range(size):
            s.append(s[-1] + nums[i])
        result = float('-inf')
        for i in range(size):
            if i+k <= size:
                result = max(result, s[i+k] - s[i])

        return result / k