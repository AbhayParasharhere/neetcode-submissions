class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        # build graph for rows
        # build graph for cols
        # cobine both topo sort order to get the actual row and col position

        res = [[0 for _ in range(k)] for _ in range(k)]

        adj_row = {u:[] for u in range(1,k+1)}
        indeg_row = [0 for u in range(k+1)]
        adj_col = {u:[] for u in range(1,k+1)}
        indeg_col = [0 for u in range(k+1)]

        for u,v in rowConditions:
            adj_row[u].append(v)
            indeg_row[v] += 1
        
        for u,v in colConditions:
            adj_col[u].append(v)
            indeg_col[v] += 1
        
        # find topo sort using kahns and give -1 when there is a cycle
        def getTopo(adj,indeg):
            # push all indeg 0 in the Q
            q = deque()
            for i,deg in enumerate(indeg):
                if i> 0 and deg == 0:
                    q.append(i)
            res = []
            while q:
                u = q.popleft()
                res.append(u)
                for v in adj[u]:
                    if indeg[v] != 0:
                        # as neighbour u was removed and added to res
                        indeg[v] -= 1
                        if indeg[v] == 0:
                            q.append(v)
            
            return res if len(res) == k else []

        topo_row = getTopo(adj_row,indeg_row)
        if not topo_row:
            return []
        
        topo_col = getTopo(adj_col,indeg_col)
        if not topo_col:
            return []
        
        # now we can extract the relavant row and col positiosn
        pos = {u: [] for u in range(1,k+1)}
        for row,u in enumerate(topo_row):
            pos[u].append(row)
        
        for col,u in enumerate(topo_col):
            pos[u].append(col)

        for u in range(1,k+1):
            row,col = pos[u]
            res[row][col] = u
        # print(topo_row,topo_col,pos,res)
        return res










