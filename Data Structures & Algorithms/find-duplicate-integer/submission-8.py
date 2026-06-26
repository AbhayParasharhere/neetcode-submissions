class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # we use a linkedin apporach
        # nums[i] goes to the next node
        # this duplicate always forms a cycle
        # first use tortise and hare to find the intersection pt
        # then again another slow from the start to find the start of the cyelc where the duplciate wil be

        slow = fast = 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        # another slow from the start to find the cycle start
        slow2 = 0

        while slow != slow2:
            slow = nums[slow]
            slow2 = nums[slow2]
        
        return slow