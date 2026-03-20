class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.strip()
        lst = ""
        ref = ""
        for i in s:
            if i == " ":
                continue
            else:
                lst += i
        s = lst
        for i in s:
            if i in ",:*@$./#!^%-_\"\'\\\{\\\}\[\]?;()`":
                continue
            else :
                ref += i
        s = ref
        s = s.lower()
        n = len(s)
        for i in range(n):
            if s[i] == s[n-i-1]:
                continue
            else: 
                return False
        return True
            
        

            