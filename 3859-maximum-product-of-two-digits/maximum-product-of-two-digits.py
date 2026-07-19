class Solution:
    def maxProduct(self, n: int) -> int:
        lst = [int(i) for i in str(n)]
        product = 0
        for i in range(len(lst)):
            for j in range(i+1, len(lst)):
                if lst[i]*lst[j] > product:
                    product = lst[i]*lst[j] 
                else:
                    continue
        return product