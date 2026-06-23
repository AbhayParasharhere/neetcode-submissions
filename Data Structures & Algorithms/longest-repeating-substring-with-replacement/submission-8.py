class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # window shrink when win length - maxfreq char > k or when we have exhauseted all k
        # we keep track of char in our window and the max freq char count as well
        # when we shrink we do have to recalcuate the max freq count if changed as well

        maxF = 0
        hmap = {}

        l = 0
        n = len(s)
        res = 0

        for r in range(n):
            # put in hmap aka window
            ch = s[r]
            hmap[ch] = hmap.get(ch,0) + 1
            maxF = max(maxF,hmap[ch])

            while (r - l + 1) - maxF > k:
                ch2remove = s[l]
                hmap[ch2remove] -=1
                if hmap[ch2remove] <= 0: del hmap[ch2remove]
                # recalc maxf as well
                maxF = max(hmap.values())
                l += 1
            # we are at all valid outputs
            res = max(res,r-l+1)
        return res