class Solution:
    def decimalRepresentation(self, n: int) -> List[int]:
        if n < 10:
            return [n] if n != 0 else []

        power = 10 ** (len(str(n)) - 1)
        first = (n // power) * power

        result = []
        if first != 0:
            result.append(first)

        result.extend(self.decimalRepresentation(n % power))
        return result