class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # bs on answer space as koko can eat banana with a rate as high as sum of all bana so it finsihes each pile in an hour
        # the lower bound is koko can eat at is 1 banana per hour
        # we return first true montonicty when koko can finish mimum in those hours provided

        def canEat(speed,time):
            time_taken = 0
            for pile in piles:
                time_taken += math.ceil(pile/speed)

            if time_taken <= time: return True
            return False

        n = len(piles)
        l = 1
        r = sum(piles)

        while l < r:
            m = (l+r) // 2
            if canEat(m,h): r = m
            else: l = m + 1
        
        return l