class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {}
        def solve(i):
            if i in cache: return cache[i]
            if i < 0: return 0
            if i == 0: return 1
            res = 0
            res += solve(i-1) + solve(i-2)
            cache[i] = res
            return res
        return solve(n)
