from collections import defaultdict,deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        # first create an adj map for faeter lookup for 1 char diffeernce for words
        # from then we will use it to create a grpah to do dfs

        mp = defaultdict(list)

        # add teh starting word in the wordlist
        wordList.append(beginWord)

        for w in wordList:
            for i in range(len(w)):
                # we can balcnk any of teh character at ith popsition in word to form a key
                left = w[0:i] + "*" +  w[i+1:]
                mp[left].append(w)
        
        adj = {}
        for values in mp.values():
            # all of the val in valeus have an undirected edge between them
            # because tehy diffre in just 1 char from each other
            if len(values) <= 1: continue
            for i in range(len(values)):
                for j in range(i+1,len(values)):
                    u = values[i]
                    v = values[j]
                    # add an undirected edge
                    if not u in adj:
                        adj[u] = []
                    if not v in adj:
                        adj[v] = []
                    
                    # add the edge
                    adj[u].append(v)
                    adj[v].append(u)

        if endWord not in adj: return 0
        # now we want to reach from teh soruce to desitination in teh shrotest way moving through our neighbours and thsi is starghtwforward bfs now
        # shortest way is literally teh amx level we reach teh destiantion in 
        visited = set()
        q = deque()
        q.append(beginWord)
        visited.add(beginWord)
        max_level = 1
        while q:
            size = len(q)
            for _ in range(size):
                u = q.popleft()
                if u == endWord:
                    return max_level
                # print('at',max_level,u)
                for v in adj[u]:
                    if v not in visited:
                        visited.add(v)
                        q.append(v)
            if q:
                max_level += 1
        return 0

