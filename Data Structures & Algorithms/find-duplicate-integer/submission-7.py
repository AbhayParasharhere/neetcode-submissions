class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # we use hare algo to find the duplicate imaging array as a linkedin list
        # to go to the enxt element it is nxt = elem[indx]
        # this linked lista nd indxing works as every elem is val is between 1, n which maps to a index

        # first find the loop interstection point
        slow,fast = 0,0

        # guranteed one dup so guarnatee in finding the intersection
        while True:
            slow = nums[slow] #advance one pointer
            fast = nums[nums[fast]] #advance 2 pointer

            if slow == fast:
                break
        
        # now slow and fasts are at the intersection point in th eloop
        # now note the start of this interection point will always be teh duplicate number
        # so we need to dfidn teh start of the loop
        # start a new slow from the start when it meets agian with slow that is at start of the loop
        slow2 = 0

        while slow != slow2:
            slow2 = nums[slow2]
            slow = nums[slow]
        
        return slow2
