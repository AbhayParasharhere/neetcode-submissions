class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # we see this as a link list
        # to travel to next it is nums[idx] to travel twice it is nums[nums[idx]]
        # so first we dfidn the existnce of the loop
        # then we again have another slow from teh start to find the cycyle's start

        slow = fast = 0

        # guarantee of a loop in this question so no worries
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        # Now slow and fast are at the loop intersection point
        # have another slow from start move until slow and slow 2 at the loop start
        slow2 = 0

        while slow != slow2:
            slow = nums[slow]
            slow2 = nums[slow2]
        
        return slow2


