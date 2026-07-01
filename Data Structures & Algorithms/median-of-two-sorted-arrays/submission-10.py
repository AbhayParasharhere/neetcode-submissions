class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # we do this by simulating teh left half if the 2 lists were merged
        # we find the boundarie nodes in both such that at boundary node in nums 1
        # everything after thae boundary node in nums 2 is less greater than it and so on
        # its like a seesaw approach, we calculate boudnary node using mid in nshorter array
        # the boundary node in other array is half elem - no of elements till medium
        # so we simulate calculating teh actual half which is separated in both array

        A, B = nums1, nums2

        if len(B) < len(A): A, B = B, A
        # A always to teh shorter

        tot = len(A) + len(B)
        half = tot // 2

        # num of elements in A can be between 0 nothing to everything or n elements
        # so we are using these bounds to simulate that
        r = len(A)
        l = 0

        while l <= r:
            m = (l+r) // 2
            o = half - m # o represnets numebr of elements taken from B array longer one

            Alt = A[m-1] if m - 1 >= 0 else float('-inf')
            # example say m is 2 we take 2 elements from A then m is ahead by 1
            # this is the case like 2nd variant of BS where answer lies in l - 1 or last false
            Art = A[m] if m < len(A) else float('inf')
            Blt = B[o-1] if o - 1 >= 0 else float('-inf')
            Brt = B[o] if o < len(B) else float('inf')

            if Alt <= Brt and Blt <= Art:
                # valid partition
                if tot % 2:
                    # odd case
                    return min(Art,Brt)
                return (min(Art,Brt) + max(Alt,Blt))/2
            elif Alt > Brt:
                # more elements taken from A need to move m back
                r = m - 1
            else:
                l = m + 1

