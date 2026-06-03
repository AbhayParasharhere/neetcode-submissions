class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # keep track of max freq char
        # length - max freq > k is our shrinkcondition for the window
        n = len(s)
        l = 0
        maxC = 0
        hmap = {}
        res = 0

        for r in range(n):
            # put in window
            if s[r] in hmap: hmap[s[r]] += 1
            else: hmap[s[r]] = 1
            # Get the max count updated
            maxC = max(maxC,hmap[s[r]])

            while (r - l + 1) - maxC > k:
                print(hmap,l,s[l])
                # reduce char from hmap and shrink window
                hmap[s[l]] -= 1
                if hmap[s[l]] <= 0: hmap.pop(s[l])
                # recalculate max
                maxC = max(hmap.values())
                l += 1
            # update our res for the longest in each valid candidate
            res = max(res,r-l+1)

        return res

