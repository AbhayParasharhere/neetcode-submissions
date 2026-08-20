class Solution:
    def maxProfit(self, prices: List[int]) -> int:
                # 3 choices on each day, buy if u dont own anything, sell if u own anything, or do nothing
        # u cannot do a buy day after selling consectutively as u can only own atmost 1 neetcde at a time

        cache ={}
        n = len(prices)

        def solve(at,own):
            if (at,own) in cache: return cache[(at,own)]
            if at >= n: return 0

            res = 0
            nothing = solve(at+1,own)
            if not own:
                buy = -prices[at] + solve(at+1,True)
                res = max(res,buy,nothing)
            else:
                sell = prices[at] + solve(at+2,False)
                res = max(res,sell,nothing)
            cache[(at,own)] = res
            return res
        return solve(0,False)