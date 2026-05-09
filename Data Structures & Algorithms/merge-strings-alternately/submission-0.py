class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l = 0
        r = 0
        res = ""
        while l < len(word1) and r < len(word2):
            res += word1[l] + word2[r]
            l += 1
            r += 1
        
        # concatenate the remaining part
        if l < len(word1):
            # print(word1[l:])
            res += word1[l:]
        if r < len(word2):
            print(word2[r:])
            res += word2[r:]
        
        return res