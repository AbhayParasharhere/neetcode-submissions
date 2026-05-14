class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        # Rversal solution
        def reverse(l,r):
            while l < r:
                nums[l],nums[r] = nums[r],nums[l]
                l, r = l + 1, r - 1
        
        # First reverse the entire list
        reverse(0,len(nums) - 1)

        # Now reverse just the first k - 1 elemnets to get teh first ection correct for teh rotated elements
        reverse(0,k-1)

        # Finally get the alst section of teh roatetd element correct by reversing from k to end
        reverse(k,len(nums) - 1)
        