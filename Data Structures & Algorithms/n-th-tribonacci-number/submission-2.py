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
        # return solve(n)
        
        prev = 1
        prev_prev = 1
        prev_prev_prev = 0
        cur = None
        if n == 1 or n == 2: return 1
        if n == 0: return 0
        # we start at n = 3
        for i in range(3,n+1):
            cur = prev_prev_prev + prev_prev + prev
            prev, prev_prev, prev_prev_prev = cur, prev, prev_prev
        return prev
