class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        V = len(edges)
        parent = [u for u in range(V+1)]
        rank = [0] * (V+1)

        def find(a):
            if parent[a] == a:
                return parent[a]
            
            parent[a] = find(parent[a])
            return parent[a]
        
        def union(a,b):
            pa = find(a)
            pb = find(b)
            if pa == pb:
                return False
            if rank[pa] > rank[pb]:
                parent[pb] = pa
            elif rank[pb] > rank[pa]:
                parent[pa] = pb
            else:
                parent[pb] = pa
                rank[pa] += 1

            return True
        
        for u,v in edges:
            # this edge formed a cycle so its the last one as well return it
            if not union(u,v):
                return [u,v]