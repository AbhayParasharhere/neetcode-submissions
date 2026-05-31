class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Space can later be made constant by using 26 + 26 char map of english
        # For now using a generic map
        # store min res as a lr tuple to extract n the end
        minRes = None
        res = deque()
        l = 0
        tmap0 = Counter(t)
        tmap = Counter(t)
        n = len(s)
        temp = {}

        # Start l at the first occurence where its a char from t
        while l < n and s[l] not in tmap:
            l += 1
        
        # First window will start from this l forward till the end as well

        for r in range(l, n):
            res += s[r]
            # reduce count from tmap if its in tmap freq and not 0
            if s[r] in tmap:
                if s[r] in temp: temp[s[r]] += 1
                else: temp[s[r]] = 1

            # Shrink when we fully match and left is not pointing to any in t
            while all(temp.get(c, 0) >= v for c, v in tmap.items()):
                # everything clear means we completly matched a candiate
                # its now a candidate for min length
                if minRes is None or len(res) < (minRes[1] - minRes[0] + 1):
                    minRes = (l, r)
                # keep popping from the res the char from the start
                # add the charcter back to tmap
                popped = res.popleft()
                if popped in temp:
                    temp[popped] -= 1
                    if temp[popped] <= 0:
                        temp.pop(popped)
                l += 1

        # Need to again check if it matches eveyrthing in tmap the final minRes
        # otehrwise return ""
        return "" if minRes is None else s[minRes[0]:minRes[1]+1]