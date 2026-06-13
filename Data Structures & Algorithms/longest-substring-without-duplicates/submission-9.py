class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # shrink when we get duplicate or a val already in hset
        # so before putting anything we can pre check and shrink window and calcule the res 

        n = len(s)
        if n <= 1: return n

        l = 0
        hset = set()
        res = 0

        for r in range(n):
            ch = s[r]
            while ch in hset:
                # as ch is not yet put but in hset we can calc res as its a valid window
                # no +1 as in window we havent yet pushed the new char at r so its off by 1
                res = max(res,r-l)
                # shrink 
                ch2remove = s[l]
                hset.remove(ch2remove)
                l += 1
            # no duplicate so we append in window
            hset.add(ch)
        # in this variant even in the end need to clacuate as evry char might be unqiue
        res = max(res,r-l+1)
        return res

        