class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # keep increasing the window, shrnk when u have used up k
        # or when your win length - most char use count > k
        # other than this eveyrthing is valid keep calc the result

        hmap = {}
        mfreq = 0
        n = len(s)
        res = 0
        l = 0

        for r in range(n):
            # put in window
            ch = s[r]
            hmap[ch] = hmap.get(ch,0) + 1
            mfreq = max(mfreq,hmap[ch])

            if r - l + 1 - mfreq > k:
                # shrink
                ch2remove = s[l]
                hmap[ch2remove] -= 1
                if hmap[ch2remove] <= 0: del hmap[ch2remove]
                # recalc max
                mfreq = max(hmap.values())
                l += 1
            # calc res as every win is valid
            res = max(res,r-l+1)
        return res
