class DSU:
    def __init__(self,n):
        self.parent = [u for u in range(n)]
        self.rank = [0] * n

    def find(self,u):
        if self.parent[u] == u:
            return self.parent[u]
        self.parent[u] = self.find(self.parent[u])
        return self.parent[u]
    
    def union(self,a,b):
        pa = self.find(a)
        pb = self.find(b)

        if pa == pb: return False

        if self.rank[pa] > self.rank[pb]:
            self.parent[pb] = pa
        elif self.rank[pb] > self.rank[pa]:
            self.parent[pa] = pb
        else:
            self.parent[pb] = pa
            self.rank[pa] += 1
        return True
class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: list[list[int]]) -> list[list[int]]:
        # 2 imp facts
        # 1- if its a critical edge the n without using it mst will icnrease
        #2-  if its a psedo critcial then there will be cases u are not using it and its still an mst so the else case of the critical edge check
        # but other important thing is including it must also result in teh mst
        # cos all thsoe useless edges which never appear in any mst are also in teh else case

        # add teh original index before sorting by wt
        for i,edge in enumerate(edges):
            edge.append(i)

        edges = sorted(edges,key=lambda x:x[2])
        print(edges)

        # find mst fx which returns a mst and takes in 2 optional param
        # to either incldue some edge or exlude some specified edge
        def findMST(n,exclude_i = -1,include_i = -1):
            dsu = DSU(n)
            mst = 0
            edge_count = 0
            if include_i != -1:
                u,v,w,i_o = edges[include_i]
                mst +=w
                dsu.union(u,v)
                edge_count += 1

            for i,(u,v,w,o_i) in enumerate(edges):
                if i == exclude_i:
                    continue
                if dsu.union(u,v):
                    mst += w
                    edge_count += 1
            
            return mst if edge_count == n -1 else float('inf')

        # now find teh mst value to compare with in teh first palce without any inclusion exlcusion
        mst = findMST(n)
        
        critical = []
        pseudo = []
        # now go through every edge
        for i,(u,v,w,o_i) in enumerate(edges):
            # exclude this edge
            if findMST(n,i,-1) > mst:
                critical.append(o_i)
            else:
                # include it and it must also be mst
                if findMST(n,-1,i) == mst:
                    pseudo.append(o_i)
        return [critical,pseudo]

        