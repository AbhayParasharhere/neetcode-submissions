class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # first lets see what happens if we dont handle duplicates specially
        res = []
        n = len(candidates)
        candidates.sort()
        def backtrack(i,comb,sum_left):
            if sum_left == 0:
                res.append(comb[:])
                return
            if i >= n: return
            elif sum_left < 0:
                return
            # val_used = set()
            for j in range(i,n):
                # if candidates[j] in val_used: continue
                if j > i and candidates[j] == candidates[j-1]: continue
                # each number atmost once so j + 1
                comb.append(candidates[j])
                # val_used.add(candidates[j])
                backtrack(j+1,comb,sum_left - candidates[j])
                comb.pop()
        backtrack(0,[],target)
        # print(res)
        return res