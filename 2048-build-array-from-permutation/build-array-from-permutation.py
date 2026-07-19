class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        num = nums.copy()
        for i in range(len(nums)):
            num[i] = nums[nums[i]]
        return num