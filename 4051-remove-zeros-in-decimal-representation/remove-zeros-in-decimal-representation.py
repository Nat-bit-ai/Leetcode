class Solution:
    def removeZeros(self, n: int) -> int:
        nums = str(n)
        nums = nums.replace("0", "")
        return int(nums)