class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n = len(s)
        tmap = Counter(t)
        l = 0
        hmap = {}
        minRes = None

        while l < n and s[l] not in tmap: l += 1

        def containsAllT():
            for k,f in tmap.items():
                if k not in hmap: return False

                f2check = hmap[k]
                if f2check < f: return False
            return True
        
        for r in range(n):
            ch = s[r]
            hmap[ch] = hmap.get(ch,0) + 1

            while containsAllT():
                # we have a valid candiate comapre for the min length
                if minRes is None or ((minRes[1] - minRes[0]) + 1) > ((r - l) + 1):
                    minRes = (l,r)
                ch2remove = s[l]
                hmap[ch2remove] -= 1
                if hmap[ch2remove] <= 0: hmap.pop(ch2remove)
                l += 1
        if not minRes: return ""
        
        return s[minRes[0]:minRes[1] + 1]
                    
