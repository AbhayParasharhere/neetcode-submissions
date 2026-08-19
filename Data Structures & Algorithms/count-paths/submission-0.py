class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        cache = {}
        def solve(i,j):
            if (i,j) in cache: return cache[(i,j)]
            if i == 0 and j == 0: return 1
            elif i < 0 or j < 0: return 0
            res = 0
            res += solve(i-1,j) + solve(i,j-1)
            cache[(i,j)] = res
            return res
        return solve(m-1,n-1)