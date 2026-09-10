class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # multisource bfs can work here
        # for handling -1 simply dont continue traversal from tehse points

        inf = 2**31 - 1

        n = len(grid)
        m = len(grid[0])

        q = deque()
        direc = [(0,1),(1,0),(-1,0),(0,-1)]
        visited = [[False for _ in range(m)] for _ in range(n)]

        # push all 0's cells as sources in Q
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    q.append((i,j))
                    visited[i][j] = True
        while q:
            level = len(q)
            for _ in range(level):
                ui,uj = q.popleft()

                for delta_i,delta_j in direc:
                    vi = ui + delta_i
                    vj = uj + delta_j
                    # print(ui,uj,'vinow',vi,vj)
                    if vi < 0 or vi >= n or vj < 0 or vj >= m or grid[vi][vj] == -1 or grid[vi][vj] == 0 or visited[vi][vj]:
                        continue
                    visited[vi][vj] = True
                    grid[vi][vj] = grid[ui][uj] + 1
                    q.append((vi,vj))
        
                


        
