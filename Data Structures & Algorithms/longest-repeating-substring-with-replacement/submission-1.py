class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        r = 0
        hmap = [0 for _ in range(26)]
        maxC = 0
        maxStr = 0
        while r < len(s):
            # put the char in map and record the max count
            idx = ord(s[r]) - ord('A')
            hmap[idx] += 1
            maxC = max(maxC,hmap[idx])

            if (r - l + 1) - maxC > k:
                # we need to remove the char at l from the map by rediucing count
                # and update the maxC potentially as well
                idx2remove = ord(s[l]) - ord('A')
                hmap[idx2remove] -= 1

                # potentially recaluciate maxC incase its freq count was reduced
                for i in range(26):
                    maxC = max(maxC,hmap[i])
                
                l += 1
            # Update max on every iteration
            maxStr = max(maxStr,r-l+1)
            r += 1
        return maxStr