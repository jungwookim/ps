# 처음 푼 풀이
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False
        hit_count = 0
        j_start = 0
        for i in range(len(s)):
            for j in range(j_start, len(t)):
                if t[j] == s[i]:
                    hit_count += 1
                    j_start = j+1
                    break
        return hit_count == len(s)

        
# 다른 풀이
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0
        
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
        
        return i == len(s)