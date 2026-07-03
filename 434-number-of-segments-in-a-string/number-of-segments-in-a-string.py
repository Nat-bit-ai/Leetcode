class Solution:
    def countSegments(self, s: str) -> int:
        s = s.strip()
        if s == "":
            return 0

        list1 = s.split(" ")
        count = 0

        for word in list1:
            if word != "":
                count += 1

        return count