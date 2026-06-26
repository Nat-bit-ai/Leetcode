class Solution:
    def sumBase(self, n: int, k: int) -> int:
        if n == 0:
            return 0
        else :
            return (n%k) + self.sumBase(int(n/k) , k)