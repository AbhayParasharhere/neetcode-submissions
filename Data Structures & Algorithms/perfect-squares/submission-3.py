class Solution:
    def numSquares(self, n: int) -> int:
        upper_lim = math.ceil(math.sqrt(n))

        # a combiantion q but we can get through permuation to save from caching i
        cache = {}
        def solve(left):
            if left in cache: return cache[left]
            if left == 0: return 0
            elif left < 0: return float('inf')

            res = float('inf')
            # start from hugher number form back for optimzation
            for j in range(upper_lim+1,0,-1):
                # we are interested in choosing perf square j*j subt from left
                # so if left would be les stahn 0 after it we can skip those branches entirely
                if left - j*j < 0: continue
                branch_res = 1 + solve(left - j*j)
                res = min(res,branch_res)
            cache[left] = res
            return res
        return solve(n)
