class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # teh node which makes upa. min ht tree is teh node along teh center of teh diameter of graph
        # diamater of tree is the lonegst path in a graph
        adj = {u:[] for u in range(n)}

        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)

        def bfs(start_node):
            visited = [False] * n
            q = deque()
            q.append(start_node)
            visited[start_node] = True

            last_node = start_node
            max_level = -1
            while q:
                level = len(q)
                max_level += 1

                for _ in range(level):
                    u = q.popleft()
                    last_node = u
                    for v in adj[u]:
                        if not visited[v]:
                            visited[v] = True
                            q.append(v)
            return (max_level,last_node)
        
        # get 1nd of diam by doing bfs and knowing the deepest level
        _,one_end_diam = bfs(0)
        diam,second_end_diam = bfs(one_end_diam)
        
        # do a dfs walk to get teh whole path from one end of diamter to teh otehr
        path = []
        visited = [False] * n
        def dfs(u,end):
            nonlocal path
            visited[u] = True
            path.append(u)

            if u == end:
                # reached the end
                # end is already apprended ealier 
                return True
            
            for v in adj[u]:
                if not visited[v]:
                    # reached teh end through thsi node
                    if dfs(v,end):
                        return True
            path.pop()
            return False
        dfs(one_end_diam,second_end_diam)
        
        # the answer is the middle 2 nodes if even else teh mid one
        mid = len(path) // 2
        # print(path,'hi',one_end_diam,second_end_diam)
        if len(path) % 2 == 0:
            return [path[mid],path[mid-1]]
        else:
            return [path[mid]]
                    
