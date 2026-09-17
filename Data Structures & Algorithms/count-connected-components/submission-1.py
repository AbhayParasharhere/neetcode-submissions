class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = [u for u in range(n)]
        rank = [0] * n

        def find(u):
            if u == parent[u]:
                return parent[u]
            parent[u] = find(parent[u])
            return parent[u]
        
        def union(a,b):
            pa = find(a)
            pb = find(b)
            if pa == pb: return False
            if rank[pa] > rank[pb]:
                parent[pb] = pa
            elif rank[pb] > rank[pa]:
                parent[pa] = pb
            else:
                parent[pb] = pa
                rank[pa] += 1
            return True
        
        for u,v in edges:
            union(u,v)
        
        comp = set()
        for u in range(n):
            comp.add(find(u))
        return len(comp)
