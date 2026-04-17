class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i] == target:
                return i
            else:
                nums.append(target)
                num = sorted(nums)
                for i in range(len(num)):
                    if num[i] == target:
                        return i

