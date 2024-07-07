class Solution:
    def climbStairs(self, n: int) -> int:
        d = [0] * 50
        d[1] = 1
        d[2] = 2
        d[3] = 3
        for i in range(1, 46):
            if i >= 4:
                d[i] = d[i - 1] + d[i - 2]
        return d[n]
