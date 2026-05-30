class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        l = 0
        hmap = set()
        maxm = 0
        if len(s) <= 1: return len(s)
        for r in range(n):
            # print(hmap,l,r,maxm)
            # Before add check
            while s[r] in hmap:
                maxm = max(maxm,r-l)
                # Keep stripping s[l] until this duplicate is removed
                # shrink window
                hmap.remove(s[l])
                l += 1
            # Add the character in window
            hmap.add(s[r])
        # This apporach requries a max reclauctaion in the end 
        maxm = max(maxm,r-l+1)
        return maxm
