class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # multi source bfs from every rotten fruit as source
        # its ets its neighbour as rotten and push them into q
        # we subtract teh total numebr of frehs fruits left everytie we have to mark fruit as rotten
        # we keep track of teh maxium levl reachd as that is our max time

        n = len(grid)
        m = len(grid[0])

        fresh = 0
        q = deque()
        time = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    # push all sources
                    q.append((i,j))
                elif grid[i][j] == 1:
                    fresh += 1
        
        # no need for marking as we only ever push grid cell 1 fruit or fresh fruit
        direc = [(0,1),(1,0),(-1,0),(0,-1)]
        while q:
            level = len(q)
            for _ in range(level):
                ui,uj = q.popleft()

                for delta_i,delta_j in direc:
                    vi = ui + delta_i
                    vj = uj + delta_j
                    if vi < 0 or vi >= n or vj < 0 or vj >= m or grid[vi][vj] != 1:
                        continue
                    # mark as rotten
                    grid[vi][vj] = 2
                    fresh -= 1
                    q.append((vi,vj))
                # after this level is done if teh q is non empty
                # increae time to do this level
            if q:
                time += 1
            
        
        return -1 if fresh != 0 else time
