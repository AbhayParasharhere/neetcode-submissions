class Solution:
    def numSquares(self, n: int) -> int:
        cache = {}

        def solve(i):
            if i in cache: return cache[i]
            if i == 0:
                return 0

            res = float('inf')
            for j in range(math.isqrt(i), 0, -1):
                branch_res = 1 + solve(i - j * j)

                # take j*j — one more square used
                branch_res = 1 + solve(i - j * j)
                res = min(branch_res, res)
                # implicit skip: the loop moving to the next j

            cache[i] = res
            return res

        return solve(n)