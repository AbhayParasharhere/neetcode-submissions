class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # first find using fitst tru bs the position higher than anything less than k and its best fit
        n = len(arr)
        l = 0
        r = n

        while l < r:
            m = (l+r) // 2
            if arr[m] >= x: r = m
            else: l = m + 1
        
        # 2 pointer to grab k elements closest
        # by nature fo first true montocity 
        # lo = l, hi = l + 1
        # our element range is only from lo + 1 to hi -1
        # window length is below
        lo = l - 1
        hi = l
        while (hi - 1) - (lo + 1) + 1 < k:
            lt = arr[lo] if 0 <= lo < n else float('-inf')
            rt = arr[hi] if 0 <= hi < n else float('inf')

            # we prefer left in case of equality
            if abs(lt - x) <= abs(rt-x):
                lo -= 1
            else:
                hi += 1
        return arr[lo+1:hi]

