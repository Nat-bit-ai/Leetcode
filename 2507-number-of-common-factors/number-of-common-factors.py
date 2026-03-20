class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        lst = []
        count = 0
        for i in range(1, a+1):
            if a % i == 0 and b % i == 0:
                lst.append(i)
            else:
                continue
        for i in lst:
            count += 1
        return count