class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        # djikstra but we track teh maxium diffrence instead of the sum
        # the route iwth teh least maximal diffrence o teh dstination from the source is put in the reuslt

        n = len(heights)
        m = len(heights[0])
        if n == 1 and m == 1: return 0
        visited = [[False for _ in range(m)] for _ in range(n)]
        res = [[float('inf') for _ in range(m)] for _ in range(n)]
        direc = [(0,1),(1,0),(-1,0),(0,-1)]

        res[0][0] = 0
        hp = []
        hp.append((0,(0,0)))
        visited[0][0] = True

        while hp:
            max_diff_so_far,(ui,uj) = heapq.heappop(hp)
            visited[ui][uj] = True
            # final pop means the reuslt is decided on this ui uj
            if res[ui][uj] < max_diff_so_far: continue
            

            for delta_i,delta_j in direc:
                vi = ui + delta_i
                vj = uj + delta_j

                if vi < 0 or vj < 0 or vi >= n or vj >= m or visited[vi][vj]:
                    continue
                cur_diff = abs(heights[ui][uj] - heights[vi][vj])
                if max(max_diff_so_far,cur_diff) < res[vi][vj]:
                    # we can put this guess
                    res[vi][vj] = max(max_diff_so_far,cur_diff)
                    heapq.heappush(hp,(res[vi][vj],(vi,vj)))
        return res[n-1][m-1]



