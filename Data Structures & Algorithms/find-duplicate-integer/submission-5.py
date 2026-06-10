class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # first floyd dedtection to find teh intersection point in teh cyce
        # slow and fast start after moving to their next from index 0
        slow = fast = nums[0]

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break
        # now we need to find teh start of the cyle
        # have another slow back from start
        # when tehse 2 slow meet again after moving, it will be at the cycle start
        slow2 = nums[0]
        while True:
            if slow == slow2:
                return slow
            slow = nums[slow]
            slow2 = nums[slow2]
        