class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # sort and then adjacent are duplicates
        nums.sort()
        res = []
        n = len(nums)
        def backtrack(i,subset):
            res.append(subset[:])

            for j in range(i,n):
                if j > i and nums[j] == nums[j-1]: continue
                subset.append(nums[j])
                backtrack(j+1,subset)
                subset.pop()
        
        backtrack(0,[])
        return res
