#User function Template for python3
class Solution:
    def minCoins(self, coins, M,summ):
        
        coins.sort(reverse=True) 
        count, i  = 0, 0
        while summ> 0 and i<M:
            if coins[i]<= summ:
                nummcoins = summ//coins[i]
                count += nummcoins
                summ -= nummcoins*coins[i]
            i +=1
        if summ == 0:
            return count
        else:
        
            return -1
