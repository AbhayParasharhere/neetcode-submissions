class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # we start from teh back -1 and ask if it can reach the last index 
        # aka teh target at that time, if eventually we arairve at start we can

        n = len(nums)
        to_reach_idx = n - 1
        if n == 1:
            return True
        if n == 2:
            if nums[0] >= 1: 
                return True
            else:
                return False
        i = n - 2
        while i >= 0:
            allowed_jump = nums[i]
            if i + allowed_jump >= to_reach_idx:
                # we can reach it so update our target to now
                # and try reaching there from teh abck
                to_reach_idx = i
            if to_reach_idx == 0:
                return True
            i -= 1
        return False
