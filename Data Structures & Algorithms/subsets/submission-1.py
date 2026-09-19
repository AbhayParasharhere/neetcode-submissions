class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        def backtrack(i,path):
            res.append(path[:])
            
            for j in range(i,n):
                # take
                path.append(nums[j])

                # explore
                backtrack(j+1,path)

                # undo for implcit skip later
                path.pop()
        backtrack(0,[])
        return res