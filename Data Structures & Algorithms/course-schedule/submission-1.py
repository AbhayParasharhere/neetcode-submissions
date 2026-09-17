class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # if cycle then its not possibel else it is 
        # lets solve using dfs or kahns

        # edges are v,u give
        adj = {u:[] for u in range(numCourses)}
        for v,u in prerequisites:
            adj[u].append(v)
        
        def dfs(u,visited,in_path):
            visited[u] = True
            in_path[u] = True

            for v in adj[u]:
                if not visited[v]:
                    # if teh ode we are about to dfs with forms a cyle tehn we return True
                    if dfs(v,visited,in_path):
                        return True
                else:
                    # v is visted but if its in path as well tehn its definely a cycle
                    # as we have already taken it into our path
                    if in_path[v]:
                        return True
            # we explored all braches with u no cycle from u neighbpurs 
            # as we are done exploring with u remove it from the path
            in_path[u] = False
            return False
    
        visited = [False] * numCourses
        in_path = [False] * numCourses
        for u in range(numCourses):
            if not visited[u]:
                if dfs(u,visited,in_path):
                    return False
        return True
            