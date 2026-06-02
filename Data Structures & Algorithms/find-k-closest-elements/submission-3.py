class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # bs to find teh correct position clossest position
        # /first true apporach
        # tehn using two pointer expand until reach k
        n = len(arr)
        l = 0
        r = n

        while l < r:
            m = (l+r) // 2
            if arr[m] >= x: r = m
            else: l = m + 1
        
        lo = l - 1
        hi = l
        res = []
        # print(l)
        while ((hi -1) - (lo + 1) + 1 ) < k:
            before = arr[lo] if lo >= 0 else float('infinity')
            after = arr[hi] if hi < n  else float('infinity')

            if abs(before - x) <= abs(after - x):
                # prefer the before over in case of equality
                res.append(before)
                lo -= 1
            else:
                res.append(after)
                hi += 1
            
        return arr[lo+1:hi]