class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        V = n
        if len(edges) != V-1: return False

        # now must not have any cycle
        # we use parent info in edges to check for this in undirected graph

        mp = {u:[] for u in range(V)}

        for u,v in edges:
            mp[u].append(v)
            mp[v].append(u)

        parent = [-1] * n
        visited = [False] * n
        
        def dfs(u,par_u):
            visited[u] = True
            parent[u] = par_u

            for v in mp[u]:
                if not visited[v]:
                    # return if any branch has a cycel
                    if dfs(v,u):
                        return True
                else:
                    # now if the current parent is not equal to parent stored there
                    # then its a cycle
                    if v != par_u:
                        return True
            return False

        # check cycel for every component
        if dfs(0, -1):
            return False # Cycle detected in the first component

        # 2. FIX: Ensure there are no isolated, hidden components
        return all(visited) 