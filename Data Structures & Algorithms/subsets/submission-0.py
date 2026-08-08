class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(i,subset):
            nonlocal res
            res.append(subset[:])
            
            for j in range(i,len(nums)):
                num = nums[j]
                subset.append(num)
                # take
                backtrack(j+1,subset)
                # undo for implicit skip
                subset.pop()
        backtrack(0,[])
        return res