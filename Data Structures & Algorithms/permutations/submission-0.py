class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        used = [0 for _ in range(n)]
        def backtrack(i,path):
            nonlocal used
            if len(path) == n:
                res.append(path[:])
                return
            # if i >= n: return

            for j in range(0,n):
                if used[j] == 1: 
                    # print('used',nums[j])
                    continue
                used[j] = 1
                path.append(nums[j])
                backtrack(j+1,path)
                path.pop()
                used[j] = 0
        
        backtrack(0,[])
        return res
            