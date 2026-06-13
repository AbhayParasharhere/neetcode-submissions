class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # shrink when the window size is greater than k
        # maintain a set in every valid window within k size if we found another element to add return true
        n = len(nums)
        if k <= 0: return False
        l = 0
        win = set()
        
        for r in range(n):
            ch = nums[r]
            if ch in win: return True
            while r - l + 1> k:
                # shrink
                win.remove(nums[l])
                l += 1
            win.add(ch)
        return False
            
