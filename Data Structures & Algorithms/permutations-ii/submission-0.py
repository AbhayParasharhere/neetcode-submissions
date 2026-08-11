class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        # sort and check for duplciaets which are adjacent
        nums.sort()
        n = len(nums)
        used = [0 for _ in range(n)]
        res = []

        def backtrack(i,path):
            nonlocal used
            if len(path) == n:
                res.append(path[:])
                return
            
            local_used = set()
            for j in range(0,n):
                # eveyr possibel combination a duplciate could produce
                # taht subtree of conmbination is already recorded by the very first 
                # member of the duplicates so dont bother with recalc with al duplicates

                # used tracks all numbers whithin a whole path and ensure no indexes are repeated in a path
                if nums[j] in local_used or used[j] == 1: continue
                local_used.add(nums[j])
                used[j] = 1
                path.append(nums[j])
                backtrack(j+1,path)
                path.pop()
                used[j] = 0
        
        backtrack(0,[])
        return res

