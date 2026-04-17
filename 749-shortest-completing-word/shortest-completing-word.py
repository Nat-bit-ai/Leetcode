from collections import Counter
class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        need = Counter(c.lower() for c in licensePlate if c.isalpha())    
        result = None
        for word in words:
            count = Counter(word.lower())
            if all(count[c] >= need[c] for c in need):
                if result is None or len(word) < len(result):
                    result = word
        return result
                
                