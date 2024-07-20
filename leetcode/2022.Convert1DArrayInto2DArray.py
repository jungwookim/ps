# 처음 푼 풀이
class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if len(original) != m * n:
            return []
        result = []
        row = []
        for i, e in enumerate(original):
            row.append(e)
            if (i+1) % n == 0:
                result.append(row)
                row = []

        return result

# 더 깔끔한 풀이
class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if len(original) != m * n:
            return []
        result = []
        for i in range(0, len(original), n):
            result.append(original[i:i+n])

        return result
