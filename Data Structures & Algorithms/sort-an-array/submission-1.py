import random
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # Using quick sort
        # idea is to randomly pick a pivot
        # Get all elements less than pivot to the left and greater to the right
        # Atleast that pivot element is sorted to teh correct position in the array now
        # Now question is how to recursively do this for all the elements while ensuring arrabged pivots stay same
        # Is it by calling this routine on teh left and right hand of the pivot recursively
        def quickSort(lo,hi):
            # Base case when an array has single element that is just teh pivto its sorted
            if lo >= hi:
                return

            idx = random.randrange(lo,hi+1)
            nums[idx],nums[lo] = nums[lo],nums[idx] 
            pivot = nums[lo]
            lt = lo + 1
            rt = hi

            while lt < rt:
                lt_e = nums[lt]
                rt_e = nums[rt]

                if lt_e > pivot and rt_e < pivot:
                    # Swap with right poinetr
                    nums[lt],nums[rt] = nums[rt],nums[lt]
                    # Advance left and right
                    lt += 1
                    rt -= 1 
                elif lt_e < pivot:
                    # Already correct on the left
                    lt += 1
                elif rt_e > pivot:
                    # Already correct on the right
                    rt -= 1
                else:
                    # pivot equal case
                    if lt_e == pivot:
                        lt += 1
                    else:
                        rt -= 1
            if nums[rt] > pivot:
                rt -= 1
            nums[lo], nums[rt] = nums[rt], nums[lo]

            # Call quick sort on left half from lo to rt pointer which is the left half
            quickSort(lo,rt - 1)
            # Quick sort on right half from lt to hi
            quickSort(rt + 1,hi)


        quickSort(0,len(nums)-1)
        return nums

