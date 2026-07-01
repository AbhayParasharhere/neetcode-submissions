class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # max window size is k
        # if window size is k + 1 slide
        # when its a valid windwo, check the condirion

        l = 0
        n = len(nums)
        r = n
        res = 0
        win = set()

        for r in range(n):
            ch = nums[r]
            if ch in win:
                return True
            win.add(ch)
            if r - l + 1 > k:
                ch2remove = nums[l]
                win.remove(ch2remove)
                l += 1
        return False