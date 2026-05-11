class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Main logic - one ptr till such that elemnet at ptr l needs to be placed 
        # (means element to the left are all correct with no duplicates )
        # i loop poitenr helps find the next elemnt which is strictly greater than to the left of till

        if len(nums) <= 1:
            return len(nums)
        
        to_put = 1
        for i in range(1,len(nums)):
            if nums[i] > nums[to_put - 1]:
                nums[to_put], nums[i] = nums[i], nums[to_put]
                to_put += 1
        return to_put