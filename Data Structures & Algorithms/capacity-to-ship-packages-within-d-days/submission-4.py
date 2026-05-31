class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # Final wt capacity will be a bianry answer space increasing
        # bw max of weights and sum of all weights to load
        # our montonic condition would be can using the m capcity
        # all packages can be shipped or not - if yes then keep shrinking back

        n = len(weights)
        l = max(weights)
        r = sum(weights) + 1

        def canShip(targetMax):
            # Greedy appoarch ship as much wt possible to target max each day
            allowedDays = days
            load = 0
            for wt in weights:
                if load + wt > targetMax:
                    allowedDays -= 1
                    load = wt
                else:
                    load += wt
            return allowedDays <= days and allowedDays > 0

        while l < r:
            m = (l+r) // 2
            if canShip(m): r = m
            else: l = m + 1
        
        return l