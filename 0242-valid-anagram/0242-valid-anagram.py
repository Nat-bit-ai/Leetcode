class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        else:
            for i in s:
                if i in t and s.count(i) == t.count(i):
                    continue
                else:
                    return False
            return True