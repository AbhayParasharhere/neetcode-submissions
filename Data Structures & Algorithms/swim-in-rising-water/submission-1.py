class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # cost is dynamic
        # we difiently need to use djikstar variant
        # but we need to ensure we also store the tiem reached in the heap as well
        # why - becuase that time reached info is necessary for future cost calculation in our path as their cost is dependent on teh time so far
        # some cost turn out negtive but tehy are not negative as tey dont help teh person in giving their time back, tehy simply dont cost anything so cost 0 is apporpiate for thos ecases
        hp = []

        neighbours = [(0,1),(1,0),(-1,0),(0,-1)]
        n = len(grid)
        m = len(grid[0])
        res = [[float('inf') for i in range(m)] for j in range(n)]
        visited = [[False for i in range(m)] for j in range(n)]

        # time_cost,original_time,(i,j)
        hp.append((grid[0][0] + 0,grid[0][0],0,(0,0)))
        res[0][0] = grid[0][0] + 0

        while hp:
            tot,C,T,(ui,uj) = heapq.heappop(hp)
            if res[ui][uj] < C + T: continue
            # popped so time is updated
            time = T + C
            # decided for this so mark it
            visited[ui][uj] = True

            for delta_i,delta_j in neighbours:
                vi = ui + delta_i
                vj = uj + delta_j

                if vi < 0 or vi >= n or vj < 0 or vj >= m or visited[vi][vj]:
                    continue
                new_cost = max(grid[vi][vj] - time,0)
                if new_cost + time < res[vi][vj]:
                    res[vi][vj] = new_cost + time
                    heapq.heappush(hp,(new_cost + time,new_cost,time,(vi,vj)))
        # print(res)
        return res[n-1][m-1]