class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        correct_sum = n * (n + 1) // 2
        actual_sum = sum(nums)
        unique_sum = sum(set(nums))
        
        missing = correct_sum - unique_sum
        duplicate = actual_sum - unique_sum
        
        return [duplicate, missing]