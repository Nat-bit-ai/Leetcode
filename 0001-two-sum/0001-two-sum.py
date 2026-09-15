class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = {}
        for i,num in enumerate(nums):
            answer = target - num
            if answer in n:
                return [n[answer],i]
            n[num] = i
        return []