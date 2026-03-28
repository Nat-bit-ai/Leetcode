class Solution:
    def reverseBits(self, n: int) -> int:
        b = []
        for i in range(32):
            b.append(str(n % 2))
            n //= 2
        res_string = "".join(b)
        return int(res_string, 2)
            
