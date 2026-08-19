class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        def solve(i,j):
            if i == 0 and j == 0: return grid[0][0]
            elif i < 0 or j < 0: return float('inf')

            # if we take top or left path see on both choices the price we pay
            # choose the minm
            res = float('inf')
            top = grid[i][j] + solve(i-1,j)
            left = grid[i][j] + solve(i,j-1)
            res = min(top,left)
            return res
        # return solve(m-1,n-1)

        dp = [[grid[i][j] for j in range(n)] for i in range(m)]
        
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0: continue
                bt = dp[i-1][j] if i - 1 >= 0 else float('inf')
                rt =  dp[i][j-1] if j - 1 >= 0 else float('inf')
                dp[i][j] = grid[i][j] + min(bt, rt)
        return dp[m-1][n-1]

