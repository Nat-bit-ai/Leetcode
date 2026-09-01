class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        aliceSizes.sort()
        bobSizes.sort()
        
        alice = sum(aliceSizes)
        bob = sum(bobSizes)
        diff = (alice - bob) // 2
        
        i, j = 0, 0
        while i < len(aliceSizes) and j < len(bobSizes):
            current_diff = aliceSizes[i] - bobSizes[j]
            if current_diff == diff:
                return [aliceSizes[i], bobSizes[j]]
            elif current_diff < diff:
                i += 1
            else:
                j += 1
        
        return []