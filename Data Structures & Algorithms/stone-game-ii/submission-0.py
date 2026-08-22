class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        # its a combination question with an availiability that doubles after every turn
        # taht availibility determines how many consective stones they can pick form start
        # initially it is 2
        # doubles by how many stone they took

        n = len(piles)
        cache = {}
        # we track botha lice and bob score
        def solve(at,a_turn,max_stones):
            if (at,a_turn,max_stones) in cache: return cache[(at,a_turn,max_stones)]
            if at >= n : return (0,0)

            res = (0,0)
            stones_taken = 0
            for j in range(at,min(at+max_stones,n)):
                stones_taken += piles[j]
                number_taken = j - at + 1
                # as stoens taken could be less than their max availibility
                # but max_stones can never decrease only increase so we use max
                new_max_stones = max(max_stones,2*number_taken)
                sub_a, sub_b = solve(j+1,not a_turn,new_max_stones)
                final = (stones_taken + sub_a,sub_b) if a_turn else (sub_a,stones_taken + sub_b)

                if a_turn and final[0] > res[0]:
                    res = final
                if not a_turn and final[1] > res[1]:
                    res = final
            cache[(at,a_turn,max_stones)] = res
            return res
        return solve(0,True,2)[0]
