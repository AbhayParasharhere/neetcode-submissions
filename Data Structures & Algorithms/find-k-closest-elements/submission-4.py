class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # use bs to find teh clsoset element position using first true
        # then expand using 2 pointers until u find k elements
        n = len(arr)
        l = 0
        r = n

        while l < r:
            m = (l+r) // 2
            if arr[m] >= x: r = m
            else: l = m + 1
        lo = l - 1
        hi = l

        while ((hi - 1) - (lo + 1) + 1) < k:
            lft = arr[lo] if lo >= 0 else float('infinity')
            rt = arr[hi] if hi < n else float('infinity')

            if abs(lft - x) <= abs(rt - x):
                lo -= 1
            else:
                hi += 1
        
        return arr[lo+1:hi]