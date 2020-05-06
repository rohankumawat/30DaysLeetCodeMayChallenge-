class Solution:
    def firstUniqChar(self, s: str) -> int:
        c = {}
        for i in s:
            if i in c:
                c[i] += 1
            else:
                c[i] = 1
        for i in range(len(s)):
            if c[s[i]] == 1:
                return i
        else:
            return -1
