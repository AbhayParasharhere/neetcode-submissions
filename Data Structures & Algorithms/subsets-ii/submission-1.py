class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # sort so that duplicates are adjcent

        nums.sort()
        res = []
        def backtrack(i,path):
            print(i)
            if i == len(nums):
                res.append(path[:])
                return
            path.append(nums[i])
            backtrack(i+1,path)
            # undo
            path.pop()

            while i + 1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            backtrack(i+1,path)
        backtrack(0,[])
        return res