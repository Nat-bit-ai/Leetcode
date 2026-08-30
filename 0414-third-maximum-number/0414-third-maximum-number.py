class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = set(nums)
        n = len(nums)
        if n < 3:
            nums = sorted(nums)
            return nums[n-1]
        else:
            nums = sorted(nums)
            return nums[n-3]