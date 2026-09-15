class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        freq = Counter(nums)    
        return max(freq , key = freq.get)