class Solution:
    def calPoints(self, operations: List[str]) -> int:
        list1 = []
        for i in operations:
            if i == "D":
                z = list1[-1]*2
                list1.append(z)
            elif i == "C":
                list1.pop()
            elif i == "+":
                list1.append(list1[-1] + list1[-2])
            elif i == "-":
                list1.append(list1[-1] - list1[-2])
            else:
                list1.append(int(i))
        return sum(list1)

