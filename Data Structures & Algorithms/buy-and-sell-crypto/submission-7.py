class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        profit = 0
        while r <= len(prices) - 1:
            profit = max(profit,prices[r] - prices[l])
            if(prices[l] >= prices[r]):
                l  = r
                r += 1
            else:
                r +=1 

        return profit