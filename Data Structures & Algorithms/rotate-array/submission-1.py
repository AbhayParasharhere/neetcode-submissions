class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Go through each element shift it to the current pos + k
        #  use modulo to calculate this final poistion to ensure elements moved beyond end move to the 
        # correct pos
        #  as we are swappingw e just need to do this till half of the array
        #  bug for odd this is happening once more than usual
        nums_copy = [*nums]
        i = 0
        while i < len(nums):
            put_at = (i + k ) % len(nums)
            nums[put_at] = nums_copy[i]
            i += 1
        