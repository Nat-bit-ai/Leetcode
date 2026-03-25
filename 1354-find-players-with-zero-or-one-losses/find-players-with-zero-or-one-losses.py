class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        lst = []
        lst2 =[]
        win = []
        loss = []
        for i in range( 0 , len(matches)):
            lst2.append(matches[i][0])
        for i in range( 0 , len(matches)):
            lst.append(matches[i][1]) 
        unique_players = sorted(set(lst + lst2))
        loss_counts = Counter(lst)
        for i in unique_players:
            count_i = loss_counts[i] 
            
            if count_i == 0:
                win.append(i)
            elif count_i == 1:
                loss.append(i)
                
        return [win, loss]
