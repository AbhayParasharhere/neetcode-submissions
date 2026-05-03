class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # nums = [2,20,4,10,3,4,5]
        # qualified sequqecne are all elements incremental by 1
        # so 2,3,4,5 and 20 and 10
        # a true sequence start does not have a num - 1 existing in the nums hasmap
        # from this logic we can create a true seq beginning array or map
        # so here it would be 2:0,10:3,20:1 :position in the array 
        # Now for each beginning true sequence we loop and search
        # now we are looking for seq + 1 element going forward if we find we increase the longest length found, if greater it is updated

        if len(nums) == 0:
            return 0
        hmap = Counter(nums)
        trueStart = set()
        for i,num in enumerate(nums):
            if num - 1 not in hmap:
                trueStart.add(num)

        longest = 1

        # Now look for longest seq length
        for start in trueStart:
            longestFound = 1
            check = start + 1
            while check in hmap:
                check = check + 1
                longestFound += 1
            if longestFound > longest:
                longest = longestFound
        return longest
        # print(hmap,trueStart,longest)
        