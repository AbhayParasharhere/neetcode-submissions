class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        cache = {}
        def solve(i):
            if i in cache: return cache[i]
            if i == n: return 0
            if i > n: return float('inf')

            # take 1 step
            res = cost[i] + min(solve(i+1),solve(i+2))
            cache[i] = res
            return res
        return min(solve(0),solve(1))