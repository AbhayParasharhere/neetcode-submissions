class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        # each land cell before adding any 4 of its edges looks up to its neighbours
        # if its neighbour is water then that edge can be added to the asnwer if not then it cant be added
        # out of bound cell act as water cell
        # we do a simple bfs for traversal in the grid
        # water cell contiute 0 to answer

        n = len(grid)
        m = len(grid[0])
        visited = [[False for _ in range(m)] for _ in range(n)]

        q = deque()
        q.append((0,0))
        visited[0][0] = True
        directions = [(0,1),(1,0),(-1,0),(0,-1)]

        # need to account separately the count for teh startingc ell
        perimeter = 0
        if grid[0][0] == 1:
            top = 1
            rt = 1 if m <= 1 or grid[0][1] == 0 else 0
            lt = 1
            bt = 1 if n <= 1 or grid[1][0] == 0 else 0
            perimeter += top + rt + lt + bt
        # print(perimeter,'start')
        while q:
            ui,uj = q.popleft()

            # water cell contribute nothing
            for delta_i,delta_j in directions:
                vi = ui + delta_i
                vj = uj + delta_j
                if vi < 0 or vi >= n or vj < 0 or vj >= m or visited[vi][vj]:
                    continue

                visited[vi][vj] = True
                q.append((vi,vj))
                if grid[vi][vj] == 0:
                    continue
                else:
                    top = 1 if (vi - 1 < 0 or grid[vi-1][vj] == 0) else 0
                    rt = 1 if (vj + 1 >= m or grid[vi][vj+1] == 0) else 0
                    lt = 1 if (vj - 1 < 0 or grid[vi][vj-1] == 0) else 0
                    bt = 1 if (vi + 1 >= n or grid[vi+1][vj] == 0) else 0
                    perimeter += top + rt + lt + bt

        return perimeter

