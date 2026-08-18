class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # allowed to repeat so j will be passed

        n = len(nums)
        cache = {}
        def solve(left):
            if left in cache: return cache[left]
            if left == 0:
                return 1
            elif left < 0:
                return 0
            
            res = 0
            for j in range(0,n):
                # take numsj
                res += solve(left-nums[j])
                # impplict skip branch later
                # we are claculating all lefes which reach the combination with dups
            cache[left] = res

            return res
        return solve(target)