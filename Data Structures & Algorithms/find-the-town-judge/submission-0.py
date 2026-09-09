class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # town judge has indegree v-1 and outgree 0 meaing he trusts nobody
        # calculate the indegree and outdegree array if any ndoe staifies this 
        # then taht evrtex is the judge

        outdeg = [0] * n
        indeg = [0] * n
        for u,v in trust:
            indeg[v-1] += 1
            outdeg[u-1] += 1
        
        for u in range(n):
            out = outdeg[u]
            ind = indeg[u]
            if ind == n -1 and out == 0:
                return u + 1 
        # print(outdeg,indeg)
        return -1