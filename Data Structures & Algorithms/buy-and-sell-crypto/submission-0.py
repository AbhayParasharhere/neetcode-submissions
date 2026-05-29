class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Keep storing the prices you move to in a set with index
        # if any price in your window prev was less than cur price
        # then you go to past and buy that day
        # you store a max as well
        n = len(prices)
        l = 0
        minP = prices[0]
        profit = 0
        # past can be a heap to track of the mnimum price at the top

        for r in range(n):
            # decide buy or not if your cur - min > 0 store in max
            if prices[r] - minP > 0:
                profit = max(profit,prices[r] - minP)
            # Update min later
            if prices[r] < minP:
                minP = prices[r]
        return profit 
            