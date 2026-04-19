class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        s = sorted(s)
        t = sorted(t)
        ret = True

        if len(s) != len(t):
            ret = False
            return ret

        if len(s) == len(t):
            for i in range(len(s)):
                if s[i] != t[i]:
                    ret = False
                    return ret
            return ret