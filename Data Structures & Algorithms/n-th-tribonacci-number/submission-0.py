class Solution:
    def tribonacci(self, n: int) -> int:
        cache = {}
        def solve(i):
            if i in cache: return cache[i]
            if i == 0: return 0
            if i ==1 or i == 2: return 1
            res = solve(i-3) + solve(i-2) + solve(i-1)
            cache[i] = res
            return res
        return solve(n)