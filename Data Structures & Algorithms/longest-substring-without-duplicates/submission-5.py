class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        n = len(s)
        res = 0
        hmap = set()

        for r in range(n):
            # Shrink condition
            while s[r] in hmap:
                hmap.remove(s[l])
                l += 1
            # unique no duplicates in map at the moment and no s[r]
            # so safe to add
            hmap.add(s[r])
            res = max(res,r-l+1)
        return res