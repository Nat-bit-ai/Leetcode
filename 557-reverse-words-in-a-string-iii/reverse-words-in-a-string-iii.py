class Solution:
    def reverseWords(self, s: str) -> str:
        list2 = []
        s1 = ""
        list1 = s.split(" ")
        for i in list1:
            list2.append(i[::-1])
        for i in list2 :
            s1 += i
            s1 += " "
        return s1.rstrip()