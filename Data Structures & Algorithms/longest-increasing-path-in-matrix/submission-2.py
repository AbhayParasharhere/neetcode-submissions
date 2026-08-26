class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        # a cell at i,j bets path doesnt depends on where u came to this cell
        # we can use this fact to build a cache that can be used if we let any cel be the startig point
        n = len(matrix)
        m = len(matrix[0])
        cache = {}
        def solve(i,j):
            if (i,j) in cache: return cache[(i,j)]
            # invalid path doesnt contibute to elength
            if i < 0 or i >= n or j < 0 or j >= m: return 0

            # can take 4 decision at any point we choose the maximum eventually at all these 4 decisions
            # but only take decision when tehy are valid or theri val greater than ccur
            cur = matrix[i][j]
            up = 1 + solve(i+1,j) if i + 1 < n and matrix[i+1][j] > cur else 0
            dn = 1 + solve(i-1,j) if i - 1 >= 0 and matrix[i-1][j] > cur else 0
            rt = 1 + solve(i,j+1) if j + 1 < m and matrix[i][j+1] > cur else 0
            lt = 1 + solve(i,j-1) if j - 1 >= 0 and matrix[i][j-1] > cur else 0

            # take the best of these 4 decisons to make the eventual optmum result
            res = max(up,dn,rt,lt)
            cache[(i,j)] = res
            return res
        
        # can be any starting point
        res = float('-inf')
        for i in range(n):
            for j in range(m):
                this_cell_best = solve(i,j)
                res = max(res,this_cell_best)
        # + 1 cos the path doenst include the current cell 
        return res + 1

        
