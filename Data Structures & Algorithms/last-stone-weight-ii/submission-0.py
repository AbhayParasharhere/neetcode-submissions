class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        # haha a trick question basically we want to find the 2 closest subset or pile of stones to total sum's half
        # the answer is the diffrence between these 2 piels
        # so 2 clsoest susbet to total / 2 and the diff is the answer
        # we can use matsh to find this exact half subste relation as well
        total = sum(stones)
        target = math.ceil(total/2)
        cache = {}
        def solve(at,so_far):
            if (at,so_far) in cache: return cache[(at,so_far)]
            if so_far >= target or at >= len(stones):
                other_pile = abs(so_far - total)
                # we fidn the first pile by the function
                return abs(so_far - other_pile)
            take = solve(at+1,so_far+stones[at])
            skip = solve(at+1,so_far)
            res = min(take,skip)
            cache[(at,so_far)] = res
            return res
        return solve(0,0)
            
