class Solution:
    def integerBreak(self, n: int) -> int:

        #  a combination question to make sum n but we can permute to save cahcing n as order doent matter nayway identical branches are cached under memo of opp order
        # but we choose teh best combination over the best product of them foudn so far
        cache = {}
        def solve(left):
            if left in cache: return cache[left]
            if left == 0:
                return 1
            elif left < 0:
                # discard these bracnhes
                return float('-inf')
            res = float('-inf')
            for j in range(1,n):
                # take the j
                if left - j < 0: continue
                branch_res = j * solve(left-j)
                res = max(res,branch_res)
            cache[left] = res
            return res
        return solve(n)
                

