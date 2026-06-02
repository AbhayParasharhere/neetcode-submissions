class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n = len(s)
        tmap = [0 for _ in range(52)]
    
        def getIdx(ch):
            return ord(ch) - ord('A') if ch.isupper() else ord(ch) - ord('a') + 26

        for ch in t:
            idx = getIdx(ch)
            tmap[idx] += 1

        l = 0
        minRes = None
        temp = [0 for _ in range(52)]

        # start l at the first char in t
        while l< len(s) and tmap[getIdx(s[l])] < 1:
            l += 1

        def tdone():
            # Check if every ch in tmap is atleast there in temp
            for ch in t:
                idx = getIdx(ch)
                atleast = tmap[idx]
                present = temp[idx]
                if present < atleast: return False
            return True

        for r in range(len(s)):
            ch = s[r]
            idx = getIdx(ch)

            #  if s[r] in tmap
            if tmap[idx] >= 1:
                if temp[idx] >= 1: temp[idx] += 1
                else: temp[idx] = 1
            
            # shrink when our temp contains all the character in t in it atleast
            while tdone():
                # candiate for min res
                if minRes is None or (r-l+1) < (minRes[1] - minRes[0] + 1):
                    minRes = (l,r)
                idxToremove = getIdx(s[l])
                temp[idxToremove] -= 1
                l += 1
        if minRes is None: return ""

        return s[minRes[0]:minRes[1]+1]
