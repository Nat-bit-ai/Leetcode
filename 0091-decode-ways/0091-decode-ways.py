class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0':
            return 0
        
        # prev2 represents dp[i-2], prev1 represents dp[i-1]
        prev2 = 1  # Base case: empty string has 1 way
        prev1 = 1  # Base case: string of length 1 (not '0') has 1 way
        
        for i in range(1, len(s)):
            current = 0
            
            # Single-digit decode: s[i] must be in '1'-'9'
            if s[i] != '0':
                current += prev1
                
            # Two-digit decode: s[i-1:i+1] must be between "10" and "26"
            two_digit = int(s[i-1:i+1])
            if 10 <= two_digit <= 26:
                current += prev2
                
            # If at any point both transitions are invalid, the string cannot be decoded
            if current == 0:
                return 0
                
            prev2 = prev1
            prev1 = current
            
        return prev1