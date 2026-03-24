class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        num3 = set(nums1)
        num4 = set(nums2)
        num5 = num3.intersection(num4)
        return list(num5)