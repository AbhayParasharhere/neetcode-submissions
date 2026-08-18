class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        tot = sum(nums)
        if tot % 2: return False

        half = tot // 2
        n = len(nums)
        cache = {}
        def solve(i,need):
            if (i,need) in cache: return cache[(i,need)]
            if need == 0: return True
            if i >= n: return False


            for j in range(i,n):
                # take and return treu on any branch
                if solve(j+1,need-nums[j]):
                    cache[(i,need)] = True
                    return True
                # implicit skip
            cache[(i,need)] = False
            return False
        return solve(0,half)