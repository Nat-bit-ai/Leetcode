class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        
        valid = []
        
        for i in words:
            ok = True
            
            for j in licensePlate:
                if j.isalpha():
                    if i.lower().count(j.lower()) < licensePlate.lower().count(j.lower()):
                        ok = False
                        break
            
            if ok:
                valid.append(i)
        
        # find shortest
        z = valid[0]
        for i in range(1, len(valid)):
            if len(valid[i]) < len(z):
                z = valid[i]
        
        return z
                
                