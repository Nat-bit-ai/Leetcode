class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        list1 = []
        list2 = ""
        for i in range(len(digits)):
            z = str(digits[i])
            list2 += z
        z = int(list2)
        z += 1
        x = str(z)
        for i in x:
            y = int(i)
            list1.append(y)
        return list1
