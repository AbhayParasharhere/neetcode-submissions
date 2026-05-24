class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def getDaysNeeded(capacity):
            d = 1
            total = 0
            for i in range(len(weights)):
                total += weights[i]
                if total > capacity:
                    d += 1
                    total = weights[i]
            return d

        l = max(weights)
        r = sum(weights) + 1

        while l < r:
            m =(l+r) //2
            if getDaysNeeded(m) <= days: r = m
            else: l = m + 1
        
        return l


