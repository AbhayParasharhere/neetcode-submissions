class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        cache = {}
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        if obstacleGrid[0][0] == 1 or obstacleGrid[m-1][n-1] == 1: return 0
        # def solve(i,j):
        #     if (i,j) in cache: return cache[(i,j)]
        #     if i == 0 and j == 0: return 1
        #     elif i < 0 or j < 0: return 0
        #     # for obstacle
        #     if obstacleGrid[i][j] == 1: return 0
        #     res = 0
        #     res += solve(i-1,j) + solve(i,j-1)
        #     cache[(i,j)] = res
        #     return res
        # return solve(m-1,n-1)

        dp = [[0 for _ in range(n)] for _ in range(m)]
        # dp i j stores the unique path to reach i, j from 0,0
        # first csolumn
        # if we encounter any obstacle then rest of that dp filling remains 0 else we fill 1
        # same logic for first row
        # first col
        for i in range(0,m):
            if obstacleGrid[i][0] == 1: break
            # there is litreally one singular way anyway
            dp[i][0] = 1
        
        for j in range(0,n):
            if obstacleGrid[0][j] == 1: break
            dp[0][j] = 1
        
        for i in range(1,m):
            for j in range(1,n):
                top = dp[i-1][j] if i - 1 >= 0 else 0
                right = dp[i][j-1] if j - 1 >= 0 else 0
                if obstacleGrid[i][j] == 1: 
                    dp[i][j] = 0
                    continue
                dp[i][j] = top + right
        return dp[m-1][n-1]
        