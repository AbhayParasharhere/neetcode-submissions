class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = [u for u in range(n)]
        rank = [0] * n
        def find(a):
            if parent[a] == a:
                return a
            parent[a] = find(parent[a])
            return parent[a]
        def union(a,b):
            p_a = find(a)
            p_b = find(b)

            if p_a == p_b:
                return False
            
            if rank[p_a] > rank[p_b]:
                parent[p_b] = p_a
            elif rank[p_b] > rank[p_a]:
                parent[p_a] = p_b
            else:
                parent[p_b] = p_a
                rank[p_a] += 1
            return True
        for u,v in edges:
            union(u,v)
        
        comp = set()
        for u in range(n):
            comp.add(find(u))
        return len(comp)
        
