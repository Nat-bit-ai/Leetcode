class Solution:
    def isHappy(self, n: int) -> bool:
        def iter(n):
            if n == 1:
                return True
            if n == 4:
                return False

            sumy = 0
            for i in str(n):
                sumy += int(i) ** 2

            return iter(sumy)

        return iter(n)