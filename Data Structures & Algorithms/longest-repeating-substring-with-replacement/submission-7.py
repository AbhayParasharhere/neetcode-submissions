class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # termination condition is window length + most frquent char > k
        # at this point we want to calculate the max length found
        n = len(s)
        l = 0
        hmap= {}
        maxf = 0
        res = 0

        for r in range(n):
            ch = s[r]
            hmap[ch] = hmap.get(ch,0) + 1
            maxf = max(hmap[ch],maxf)

            while (r - l + 1) - maxf > k:
                # shrink as we have exhausted all of k's
                ch2remove = s[l]
                hmap[ch2remove]-= 1
                if hmap[ch2remove] <= 0: del hmap[ch2remove]
                # recalc maxf
                maxf = max(hmap.values())
                l += 1

            # calculate res on every valid window iteration
            res = max(res,r-l+1)

        return res

            

