class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Using the optimal binary search apporach using partition
        # Basically we are forming teh valid left partition across both array
        # return the median element as you get the valid partition figured out
        # they are just the max of your left partioon figured
        # and teh min of the right partiion
        # overall in teh end due tot his we have a valid left partition
        # we control the comparision of a left with beright 
        # to move both our i and j pointer which are indexes of our valid partiion
        # that satifies the left partion condition such that  ith position a left <= b right
        A,B = nums1,nums2
        half = (len(nums1) + len(nums2)) // 2

        if len(A) > len(B):
            A,B = B,A
            # A always points to the shorter

        l,r = -1, len(A) - 1

        while True:
            # i tracks the index of the last element partiton from A
            # standard bs l pointer is responsibel for this as moving this 
            # moves both teh end index from A and B which constututes the valid left partition
            i = (l+r) // 2
            j = half - i - 2 # -2 since both i and j are 0 indexed start

            Aleft = A[i] if i >= 0 else float('-infinity')
            Aright = A[i+1] if i + 1 < len(A) else float('infinity')
            Bleft = B[j] if j>= 0 else float('-infinity')
            Bright = B[j+1] if j + 1 < len(B) else float('infinity')

            if Aleft <= Bright and Bleft <= Aright:
                # Valid left partition and conatins enough elements so its full
                if (len(A) + len(B)) % 2:
                    # odd case
                    return float(min(Aright,Bright))
                else:
                    return float((max(Aleft,Bleft)+min(Aright,Bright)) / 2)
            elif Aleft > Bright:
                # A left has elements which are greater move r back
                # so that m which is the index pointer of left partion go back
                # this removes the greater element from Aand gets more element from B instead
                r = i - 1
            else:
                # B left has gretaer element - we need less from B and move from A
                l = i + 1
            
