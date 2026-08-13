class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        tot = sum(matchsticks)
        if tot % 4: return False
        req_sum = tot // 4
        sticks = sorted(matchsticks, reverse=True)
        n = len(sticks)
        if sticks[0] > req_sum: return False
        taken = [False] * n

        def backtrack(at, sum_left, parts_found):
            if sum_left == 0:
                if parts_found == 3:
                    return True
                if backtrack(0, req_sum, parts_found + 1):
                    return True
                return False
            if sum_left < 0 or at >= n: return False
            for i in range(n):
                if taken[i]: continue
                if i > 0 and sticks[i] == sticks[i-1] and not taken[i-1]:
                    continue
                taken[i] = True
                sum_left -= sticks[i]
                if backtrack(i+1, sum_left, parts_found): return True
                taken[i] = False
                sum_left += sticks[i]
            return False

        return backtrack(0, req_sum, 0)