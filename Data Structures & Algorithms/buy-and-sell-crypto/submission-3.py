class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        profit = 0
        i = 0
        lowestP = prices[i]
        maxProfit = prices[i] - lowestP

        for i in range(len(prices)):
            if prices[i] < lowestP:
                lowestP = prices[i]
            tempMaxProfit = prices[i] - lowestP
            if tempMaxProfit > maxProfit:
                maxProfit = tempMaxProfit
        return maxProfit


        # dif = 0
        # tempDif = 0

        # for i in range(len(prices)):
        #     for j in range(i+1,len(prices)):
        #         tempDif = prices[j] - prices[i]
        #         if tempDif > dif:
        #             dif = tempDif

        # if dif < 0:
        #     return 0

        # return dif