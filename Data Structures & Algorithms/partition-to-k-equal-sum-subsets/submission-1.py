class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        tot = sum(nums)
        if tot % k: return False
        sum_req = tot // k
        nums.sort(reverse=True)
        n = len(nums)
        marked = [False] * n
        # descending + dedup to prune the backtracking tree

        def backtrack(at,sum_left,parts_formed):
            if sum_left == 0:
                # if we enter it again and parts is k -1 
                # we have exactly formed k parts
                if parts_formed == k - 1:
                    return True
                if backtrack(0,sum_req,parts_formed+1):
                    return True
                return False
            if at >= n or sum_left < 0: return False
            for i in range(0,n):
                if marked[i]: continue
                # the first duplicate was not used int he pairing so safe to skip all dups
                if i > 0 and nums[i] == nums[i-1] and not marked[i-1]:
                    continue
                marked[i] = True
                sum_left -= nums[i]
                # if any of them return true we are done
                if backtrack(i+1,sum_left,parts_formed):
                    return True
                sum_left += nums[i]
                marked[i] = False
            return False
        return backtrack(0,sum_req,0)


