class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        l = 0
        n = len(s)
        win = {}

        # shrink when window contains duplicate

        for r in range(n):
            # first cehck before adding to ensure no dupl
            ch = s[r]
            while s[r] in win:
                ch2remove = s[l]
                win[ch2remove] -= 1
                if win[ch2remove] <= 0: del win[ch2remove]
                l += 1
            # add to window now
            win[ch] = win.get(ch,0) + 1
            # all are valid window with no dups
            res = max(res,r-l+1)
        return res

