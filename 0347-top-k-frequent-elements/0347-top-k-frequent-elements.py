class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        freq = sorted(freq, key = freq.get , reverse = True)
        res = []
        for i in range(k):
            res.append(freq[i])
        return res
            
