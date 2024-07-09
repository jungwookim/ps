from typing import List

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        lt, rt = 0, len(letters) - 1

        while lt <= rt:
            mid = lt + (rt - lt) // 2
            if letters[mid] > target:
                rt = mid - 1
            else:
                lt = mid + 1

        return letters[lt % len(letters)]
    