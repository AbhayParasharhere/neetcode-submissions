class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tmap = Counter(t)
        res = None

        n = len(s)
        l = 0
        hmap = {}
        # start l at the first char in t
        while l < n and s[l] not in tmap:
            l += 1

        def contains_t():
            # uses teh hmap for comapring against tmap must contain atleast all of tmap
            for k,f in tmap.items():
                if k not in hmap: return False
                else:
                    if hmap[k] < f: return False
            
            return True

        
        for r in range(n):
            # put in window
            hmap[s[r]] = hmap.get(s[r],0) + 1

            while contains_t():
                # we have now a candidate
                if res is None or ((res[1] - res[0]) + 1) > ((r - l )+ 1):
                    res = (l,r)
                # reduce the frequency from teh window map as well
                hmap[s[l]] = hmap.get(s[l],0) - 1
                if hmap[s[l]] <= 0: hmap.pop(s[l])
                l += 1
        if not res: return ""
        return s[res[0]:res[1] + 1]
            
            


