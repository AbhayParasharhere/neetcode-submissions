class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def getDaysNeeded(capacity):
            d = 1
            total = 0
            for w in weights:
                if w > capacity:
                    return float('inf')
                elif w + total > capacity:
                    d += 1
                    total = w
                else:
                    total += w
            return d
        l = 0
        r = sum(weights) + 1

        while l < r:
            m =(l+r) //2
            if getDaysNeeded(m) <= days: r = m
            else: l = m + 1
        
        return l


