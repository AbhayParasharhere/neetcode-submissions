class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # Max window size is k
        # if the element tobe put is within htat window return True
        # if window size is greater than k then shrink
        win = set()
        l = 0
        if k <= 0: return False

        for r in range(len(nums)):
            if nums[r] in win:
                return True
            
            while r - l + 1 > k:
                win.remove(nums[l])
                l += 1
            win.add(nums[r])
        return False
            
