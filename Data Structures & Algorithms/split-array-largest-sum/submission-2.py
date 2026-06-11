class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        # our montonic condiition is in the answer space
        # such that the asnwer space that our splitting done can be the minimum or greater than it
        # greater than it until we choose the partion whihc the whole array or sum of the whole array
        # our least possible minimum sum is the largest element in the whole arry taht we split every element and the alrgest stiits by itself is the largets sum
        # some answer spaces wont be possibel with k partitions available that is our false
        # who are psosible theya re out true condition we hunt for first true
        n = len(nums)
        l = max(nums)
        r = sum(nums)

        def possible(m):
            # greedy approach to use all k bars to split in the max things we can fit not exeeding m
            splits = k - 1
            tot = 0
            for num in nums:
                if tot + num > m:
                    splits -= 1
                    tot = num
                else:
                    tot += num
            return splits >= 0


        while l < r:
            m = (l+r) // 2

            if possible(m): r = m
            else: l = m + 1
        return l
        