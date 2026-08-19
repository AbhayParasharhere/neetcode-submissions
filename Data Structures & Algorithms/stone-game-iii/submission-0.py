class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        a_score = 0
        b_score = 0
        cache = {}
        def solve(i,active):
            if (i,active) in cache: return cache[(i,active)]
            if i >= n:
                return (0,0)
            
            # for 3 choices of extedning their current stone count up to 3
            res_a = None
            res_b = None
            stones_taken = 0
            for k in range(3):
                if i + k >= n: break
                stones_taken += stoneValue[i+k]
                sub_a, sub_b = solve(i+k+1,not active)
                if active:
                    cand_a,cand_b = stones_taken + sub_a,sub_b
                    # cur turn for a so maximse from all my possible turns
                    if res_a is None or cand_a > res_a:
                        res_a,res_b = cand_a, cand_b
                    
                else:
                    # turn for b, throw teh otehr res
                    cand_a,cand_b = sub_a,stones_taken + sub_b
                    if res_b is None or cand_b > res_b:
                        res_a,res_b = cand_a, cand_b
            cache[(i,active)] = (res_a,res_b)
            return cache[(i,active)]
        a,b = solve(0,True)
        return "Alice" if a > b else("Bob" if b > a else "Tie")
