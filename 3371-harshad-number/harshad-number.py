class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        c = 0
        for i in str(x):
            c += int(i)
        if x % c == 0:
            return c
        else:
            return -1