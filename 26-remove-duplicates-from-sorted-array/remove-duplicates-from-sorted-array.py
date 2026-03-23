class Solution:
    def removeDuplicates(self, nums):
        unique = sorted(set(nums))
        nums[:len(unique)] = unique
        return len(unique)