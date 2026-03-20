class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        s = s.split(" ")
        s = s[-1]
        count = 0
        for suii in s:
            count += 1
        return count

