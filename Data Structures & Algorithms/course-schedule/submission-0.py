class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # use bfs to find teh topo sort
        # if its possible then return True else return False
        # basically urun bfs from all the indegree u vertex as teh source
        # standard bfs and when u are popping just push into topo order result
        # if the length of the final topo is not equal to all vertices its a cycle that we dient take

        V = numCourses
        mp = {u:[] for u in range(V)}
        indeg = [0] * V
        # push all indeg 0 to q
        for v,u in prerequisites:
            mp[u].append(v)
            indeg[v] += 1
        
        q = deque()
        topo = []
        for u,deg in enumerate(indeg):
            if deg == 0:
                q.append(u)

        while q:
            u = q.popleft()
            topo.append(u)
            for v in mp[u]:
                # since my parent u was just popped off so my indeg is reduced by 1
                indeg[v] -= 1
                if indeg[v] == 0:
                    q.append(v)
        return True if len(topo) == V else False
