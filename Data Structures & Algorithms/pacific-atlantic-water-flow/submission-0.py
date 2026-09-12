class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # have a vsisitd array for cells who are connected to pacific
        # run dfs on these starting row and start ciolumh so this depedncy is trickeld down to neighbour whoa re greater than it
        # siilary run dfs for atlantic conncetd neighbours and mark theri own neighbours whoa re connected
        n = len(heights) 
        m = len(heights[0])
        pacific_visited = [[False for _ in range(m)] for _ in range(n)]
        atlantic_visited = [[False for _ in range(m)] for _ in range(n)]

        # run dfs through the cells who are first row and first columna nd mark eveyr neighbour whoa re greater as pacific
        neighbours = [(0,1),(1,0),(-1,0),(0,-1)]

        def dfs(i,j,visited):
            visited[i][j] = True
            for delta_i,delta_j in neighbours:
                vi = i + delta_i
                vj = j + delta_j
                if vi < 0 or vi >= n or vj < 0 or vj >= m: continue
                if not visited[vi][vj] and heights[vi][vj] >= heights[i][j]:
                    dfs(vi,vj,visited)
    
        # first row
        for col in range(m):
            if not pacific_visited[0][col]:
                dfs(0,col,pacific_visited)
        
        # first col
        for row in range(n):
            if not pacific_visited[row][0]:
                dfs(row,0,pacific_visited)
        
        # last col
        for row in range(n):
            if not atlantic_visited[row][m-1]:
                dfs(row,m-1,atlantic_visited)

        # last row
        for col in range(m):
            if not atlantic_visited[n-1][col]:
                dfs(n-1,col,atlantic_visited)
        
        res = []
        for i in range(n):
            for j in range(m):
                if pacific_visited[i][j] and atlantic_visited[i][j]:
                    res.append([i,j])

        return res
