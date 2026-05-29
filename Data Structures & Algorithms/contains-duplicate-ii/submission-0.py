class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # Growing sizing window porb
        l = 0
        window = set()
        for r in range(len(nums)):
            if nums[r] in window and r > 0:
                return True
            # grow window 
            window.add(nums[r])
            while r - l + 1 >= k + 1:
                # At this point shrink window
                window.remove(nums[l])
                l += 1
        return False


            