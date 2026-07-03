class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"

        if num < 0:
            num += 2**32

        digits = "0123456789abcdef"

        def dfs(n):
            if n == 0:
                return ""
            return dfs(n // 16) + digits[n % 16]

        return dfs(num)