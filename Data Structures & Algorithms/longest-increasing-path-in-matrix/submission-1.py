class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        m = len(matrix[0])

        # we try all possible starting points, and sicne the best path increasing is independent of how we got to that cell our cache will save us a lot of computations

        # give the best path longest increasing for the given cell irresptive fo how we got here
        cache = {}
        def solve(i,j):
            if (i,j) in cache: return cache[(i,j)]
            if i >= n or j >= m or i < 0 or j < 0: return 0
            cur_val = matrix[i][j]

            # travel all possible paths at the same time, choose where u can make the longest from tehm all
            up, down, rt, lt = 0,0,0,0
            if i+1 < n and matrix[i+1][j] < cur_val:
                up = 1 + solve(i+1,j)
            if i-1 >= 0 and matrix[i-1][j] < cur_val:
                down = 1 + solve(i-1,j)
            if j+1 < m and matrix[i][j+1] < cur_val:
                rt = 1 + solve(i,j+1)
            if j-1 >= 0 and matrix[i][j-1] < cur_val:
                lt = 1 + solve(i,j-1)
            res = max(up,down,rt,lt)
            cache[(i,j)] = res
            return res 
        res = 0
        for i in range(n):
            for j in range(m):
                cur_cell_res = solve(i,j)
                res = max(res,cur_cell_res)
        
        return res + 1



