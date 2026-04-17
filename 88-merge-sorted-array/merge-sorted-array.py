class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        list1 = []
        for i in range(m):
            list1.append(nums1[i])
        for i in range(n):
            list1.append(nums2[i])
        list1 = sorted(list1)
        for i in range(m + n):
            nums1[i] = list1[i]
        return nums1