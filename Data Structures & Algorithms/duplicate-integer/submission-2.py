class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if not nums: return False
        hmap = set()
        for num in nums:
            if num in hmap: return True
            hmap.add(num)
       # print(hmap)
        return False