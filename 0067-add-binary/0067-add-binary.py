class Solution:
    def addBinary(self, a: str, b: str) -> str:
        def bin_str_to_int(num):
            result = 0
            for i in range(len(num)):
                result += int(num[len(num)-i-1]) * (2**i)
            return result

        def int_to_bin_str(num):
            if num == 0:
                return "0"
            digits = []
            while num > 0:
                digits.append(str(num % 2))
                num //= 2
            return ''.join(reversed(digits))

        a = bin_str_to_int(a)
        b = bin_str_to_int(b)
        c = a + b
        return int_to_bin_str(c)