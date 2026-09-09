class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # can solve using dsu or simply how many componets by running dfs and marking
        n = len(grid)
        m = len(grid[0])

        comp = 0
        neigh = [(1,0),(0,1),(-1,0),(0,-1)]
    
        def dfs(i,j):
            # mark as visited
            grid[i][j] = "V"
            # visit all neighbopurs who are unviisted
            for delta_i,delta_j in neigh:
                vi = delta_i + i
                vj = delta_j + j
                if vi < 0 or vi >= n or vj < 0 or vj >= m or grid[vi][vj] == "V" or grid[vi][vj] == "0":
                    continue
                else:
                    dfs(vi,vj)
        for i in range(n):
            for j in range(m):
                # visted is marked by V and 0 is water so both are skipped implictly
                if grid[i][j] == "1":
                    dfs(i,j)
                    comp += 1
        return comp
        