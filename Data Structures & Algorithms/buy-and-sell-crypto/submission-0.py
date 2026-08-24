class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit = 0

        curmin = prices[0]
        
        for i in range(len(prices)):
            curmin = min(curmin,prices[i])

            curprofit = prices[i] - curmin

            maxprofit = max(curprofit,maxprofit)

        return maxprofit

