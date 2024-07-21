class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        i, j = 0, 0
        ss = []
        tt = []
        while i < len(s) or j < len(t):
            if i < len(s):
                if s[i] == "#":
                    if ss:
                        ss.pop()
                else:
                    ss.append(s[i])
            if j < len(t):
                if t[i] == "#":
                    if tt:
                        tt.pop()
                else:
                    tt.append(t[i])
            i += 1
            j += 1
        return "".join(ss) == "".join(tt)