class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # as you are going keep track of the min and the max profit
        minPr = float('infinity')
        maxProfit = 0
        l = 0
        # condition to shrink is when we find a price less than min
        # shrink windo till there

        for r in range(len(prices)):
            minPr = min(minPr,prices[r])

            # shrink while our minimum poirce is greater than current
            while prices[l] > prices[r]:
                l += 1
            # l points to the minimum price so far and is guaranteed before
            profitThisDay = prices[r] - prices[l]
            maxProfit = max(maxProfit,profitThisDay)
        return maxProfit
