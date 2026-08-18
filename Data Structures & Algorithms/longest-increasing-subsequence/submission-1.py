from sortedcontainers import SortedDict
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        # cache = {}
        # def solve(i,last_num):
        #     if (i,last_num) in cache: return cache[(i,last_num)]
        #     if i >= n: return 0

        #     # take case only if this num is less tahn last num
        #     skip = solve(i+1,last_num)
        #     take = 0
        #     if last_num is None or nums[i] > last_num:
        #         take = 1 + solve(i+1,nums[i])
        #     cache[(i,last_num)] = max(take,skip)
        #     return cache[(i,last_num)]
        # return solve(0,None)

        # now dp appraoch with sorted dict
        # key is the num itself and value is the length of longest chain for that
        sd = SortedDict()
        res = 1
        # bisect right gives the num after the first duplicate which is palce for the req elemnt
        # bisec left points to the very first duplicate 

        for i in range(0,n):
            # get the closest neighbour which is just less than us in key
            our_key = nums[i]

            closest_neighbour_after = sd.bisect_left(our_key)
            closest_neigh_sum = sd.peekitem(closest_neighbour_after - 1)[1] if closest_neighbour_after > 0 else 0
            my_sum = 1 + closest_neigh_sum

            # before putting my resposnibility to clean any key greater than me but sum less tahn me
            greater_key = sd.bisect_right(our_key)
            while greater_key < len(sd) and sd.peekitem(greater_key)[1] <= my_sum:
                sd.popitem(greater_key)
            sd[our_key] = max(sd.get(our_key,my_sum),my_sum)
            res = max(res,sd[our_key])
        return res



