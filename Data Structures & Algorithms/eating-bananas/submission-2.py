class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def getTimeToEat(v):
            time = 0
            pile = 0
            while pile < len(piles):
                pile2eat = piles[pile]
                time += max(math.ceil(pile2eat / v),1)
                pile += 1
            return time

        l = 1
        r = max(piles) + 1

        while l < r:
            m = (l+r) // 2
            if getTimeToEat(m) <= h: r = m
            else: l = m + 1
        return l
        
