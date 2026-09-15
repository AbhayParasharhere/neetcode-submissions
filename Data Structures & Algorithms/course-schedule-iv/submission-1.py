class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # first lets create the graph
        V = numCourses
        mp = {u:[] for u in range(V)}
        prereq_to = {u:set() for u in range(V)}

        for u,v in prerequisites:
            mp[u].append(v)
            prereq_to[u].add(v)
        
        # now we can dfs from the query to see if its in teh path if it is then yes
        # its a pre-req but first we can check if its a direct edge from their
        # if it is then good but if not we do a dfs search and to reduce repeated work
        # we addd it to teh pre-req of teh node along teh path
        # so we dont have to repeat thsi dfs again
        res = [False] * len(queries)
        visited = [False] * V

        def dfs(u):
            # base case nothing left in ad list leaf node
            if visited[u]:
                return prereq_to[u]
            if not mp[u]:
                return []
            
            visited[u] = True

            for v in mp[u]:
                for far_nghbr in dfs(v):
                    prereq_to[u].add(far_nghbr)
            
            return prereq_to[u]

        for i,(u,v) in enumerate(queries):
            res[i] = v in dfs(u)
        return res