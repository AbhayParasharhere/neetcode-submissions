class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        def backtrack(i,so_far):
            nonlocal res
            res += so_far
            
            for j in range(i,n):
                # take
                so_far = so_far ^ nums[j]
                backtrack(j+1,so_far)
                # undo
                so_far = so_far ^ nums[j]
        
        backtrack(0,0)
        return res
