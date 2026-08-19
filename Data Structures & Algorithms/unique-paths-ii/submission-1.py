class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1: return 0
        cache = {}
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        def solve(i,j):
            if (i,j) in cache: return cache[(i,j)]
            if i == 0 and j == 0: return 1
            elif i < 0 or j < 0: return 0
            # for obstacle
            if obstacleGrid[i][j] == 1: return 0
            res = 0
            res += solve(i-1,j) + solve(i,j-1)
            cache[(i,j)] = res
            return res
        return solve(m-1,n-1)