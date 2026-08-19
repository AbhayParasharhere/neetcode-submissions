class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        cache = {}

        # a combination q with no repeat on prices and we alternate between - and + to return teh profit eventually - initially buy so porfit is -ve whatevr we buy
        def solve(i,own):
            if (i,own) in cache: return cache[(i,own)]
            if i >= n: return 0
            profit = 0

            for j in range(i,n):
                branch_profit = 0
                if own:
                    branch_profit = prices[j] + solve(j+2, False)
                else:
                    branch_profit = -prices[j] + solve(j+1, True)
                profit = max(profit,branch_profit)
            cache[(i,own)] = profit
            return profit
        return solve(0,False)