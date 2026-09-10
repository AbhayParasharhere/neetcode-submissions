class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # lets use stack dfs for practice can also use bfs or dsu
        # we keep track of max size stack has at any point as the final answer of the biggest componet
        # mark -1 for visietd

        n = len(grid)
        m = len(grid[0])
        res = 0
        directions = [(0,1),(1,0),(-1,0),(0,-1)]

        def dfs(i,j):
            nonlocal res
            # mark then visit neighbours
            stack = []
            stack.append((i,j))
            # no need to amrk initially ahndled by fx intenionally left
            area = 1
            while stack:
                # peek and mark
                ui,uj = stack[-1]
                grid[ui][uj] = -1
                

                for delta_i,delta_j in directions:
                    vi = ui + delta_i
                    vj = uj + delta_j
                    if vi < 0 or vi >= n or vj < 0 or vj >= m or grid[vi][vj] == -1 or grid[vi][vj] == 0:
                        # reached the end so pop
                        continue
                    else:
                        # push qualified neighbours
                        stack.append((vi,vj))
                        area += 1
                        break
                else:
                    stack.pop()

            res = max(res,area)

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    dfs(i,j)
        
        return res