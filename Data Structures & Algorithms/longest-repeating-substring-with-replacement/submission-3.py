class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # we maintain a most freq char count and a freq map
        # we know that when winlength - most Freq must be less than or equal to k
        # taht is we used all our k to get the max string to check
        # more than this and we will have to srink back
        # next candidate to check we can just reduce the left most until we are in the bounds
        # to do this we must reduce the freq of that removed element at l from map as well

        maxC = 0
        hmap = [0 for _ in range(26)]
        l = 0
        maxRes = 0

        for r in range(len(s)):

            # put in the window
            idx = ord(s[r]) - ord('A')
            hmap[idx] += 1
            maxC = max(maxC,hmap[idx])
            while (r - l + 1) - maxC > k:
                # Shrink time by reducing char at l 
                idx2remove = ord(s[l]) - ord('A')
                # guaranteed to be there
                hmap[idx2remove] -= 1
                l += 1
                # Recalculate maxC in case it was reduced
                maxC = max(hmap)
            # Update final res everything is valid as win length is atmost k
            maxRes = max(maxRes,r-l+1)
        return maxRes



