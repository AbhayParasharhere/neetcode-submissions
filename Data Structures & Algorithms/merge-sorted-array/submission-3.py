class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if m == 0:
            for i in range(n):
                nums1[i] = nums2[i]
    
        l = m - 1
        r = n - 1
        to_fill = m + n - 1
        filled = 0
        while r>= 0 and l >= 0:
            # put the greater element at to_fill
            if nums1[l] > nums2[r]:
                nums1[l], nums1[to_fill] = nums1[to_fill], nums1[l]
                l -= 1
                filled += 1
                to_fill -= 1
            else:
                nums2[r], nums1[to_fill] = nums1[to_fill], nums2[r]
                r -= 1
                filled += 1
                to_fill -= 1

        # Now check if tehre are any elemnets left in r to replace the nums 1 from start
        # since nums 2 is sorted teh result would be sorted
        if r >= 0:
            for i in range(r+1):
                nums1[i] = nums2[i]
                r -= 1
