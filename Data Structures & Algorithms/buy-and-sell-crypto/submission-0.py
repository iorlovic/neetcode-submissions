class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        dif = 0
        tempDif = 0

        for i in range(len(prices)):
            for j in range(i+1,len(prices)):
                tempDif = prices[j] - prices[i]
                if tempDif > dif:
                    dif = tempDif

        if dif < 0:
            return 0

        return dif