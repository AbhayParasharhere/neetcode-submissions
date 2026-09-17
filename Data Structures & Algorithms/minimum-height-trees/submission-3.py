class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # first find teh diametr node then find teh path of the diameter and return teh middle nodes

        adj = {u:[] for u in range(n)}
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)

        
        def bfs(u):
            visited = [False] * n
            q = deque()
            q.append(u)
            visited[u] = True
            
            last_node = u
            max_level = -1
            while q:
                size = len(q)
                max_level += 1
                for _ in range(size):
                    popped_u = q.popleft()
                    last_node = popped_u
                    for v in adj[popped_u]:
                        if not visited[v]:
                            visited[v] = True
                            q.append(v)
            return (max_level,last_node)
        
        _,one_end_diam = bfs(0)
        diam,other_end_diam = bfs(one_end_diam)
        visited = [False] * n
        # now a dfs search to find the whole path of the diameter
        path = []
        def dfs(u,end):
            nonlocal path
            path.append(u)
            visited[u] = True
            if u == end:
                # mark thsi apth true so only this path is ever counted
                return True

            for v in adj[u]:
                if not visited[v]:
                    # check if any of these v can be appended and produces the final
                    if dfs(v,end):
                        return True
            # remove u from the path as no branch from u could reach the end
            # we need to recurse and try other options
            path.pop()
            return False
        dfs(one_end_diam,other_end_diam)
        mid = len(path) // 2
        # print(path)
        if len(path) % 2 == 0:
            return [path[mid-1],path[mid]]
        else:
            return [path[mid]]