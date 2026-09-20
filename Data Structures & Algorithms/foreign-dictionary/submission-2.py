from collections import deque
class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # we need to find teh topo sort after we build teh graph
        # the way to build teh edges is teh first mismatch cahracter in a pair that is 
        # defintely an edge we can say due to the pairing order 
        # we cant say anythig after the first mismatch charcatcer
        # special case taht if comapring pair A before pair B and pair B is a prefix but larger we return "" rightawy

        # first find all vertices which are the distinct character we find in all the words

        # we can build vertex set as we are vuilding the edges
        n = len(words)
        vertex_set = set()
        for word in words:
            for ch in word:
                vertex_set.add(ch)
        adj = {}
        for i in range(n-1):
            pair_a = words[i]
            pair_b = words[i+1]
            for p in range(len(pair_a)):
                ch_1 = pair_a[p]
                # special case of prefix we dont need to worry about uneqal case as we always break in 1 uneqal char
                if p >= len(pair_b):
                    return ""
                    
                ch_2 = pair_b[p]
                # print('comparing ch',ch_1,ch_2)
                if ch_1 != ch_2:
                    # we add an edge and teh vertices
                    if ch_1 not in adj:
                        adj[ch_1] = set()
                    if ch_2 not in adj:
                        adj[ch_2] = set()
                    # based on pairing order we confirm the wdge ch_1-> ch_2
                    adj[ch_1].add(ch_2)
                    # we are done compairing the pairs move on
                    break
            # after comapirng pari finished if no uneqal cahr found

        # now we just need to find teh topo order we can use kahns or dfs 
        # we need to check for cycle as well 

        q = deque()
        indegree = {u: 0 for u in vertex_set}
        # add all vertex from veretx set whose edges were neevr there

        for u in vertex_set:
            if u not in adj:
                adj[u] = set()

        # get all indegrees
        for u in adj:
            for v in adj[u]:
                indegree[v] += 1
        

        # append all the vertex of indegree 1 initially   
        # print(vertex_set,adj)
        for v,indeg in indegree.items():
            if indeg == 0:
                q.append(v)
        res = ""
        while q:
            u = q.popleft()
            res += u

            for v in adj[u]:
                # as parent u was processed
                indegree[v] -= 1
                if indegree[v] == 0:
                    q.append(v)
        if len(res) != len(vertex_set):
            return ""
        return res