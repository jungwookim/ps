class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # O(NlogN)
        # square_nums = [num*num for num in nums]
        # return sorted(square_nums)

        # O(N)
        lt, rt = 0, len(nums) - 1
        result = [0] * len(nums)
        pos = len(nums) - 1

        while lt <= rt:
            print(lt, rt)
            lv, rv = nums[lt], nums[rt]
            if abs(lv) > abs(rv):
                result[pos] = lv * lv
                lt += 1
            else:
                result[pos] = rv * rv
                rt -= 1
            pos -= 1

        return result