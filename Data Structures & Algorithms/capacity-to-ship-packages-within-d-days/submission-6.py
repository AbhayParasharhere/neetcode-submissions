class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # weight capcity can be sum of all weights which is its right bound here
        # or it could be the max of the weights otherwise anything less would not be possible
        # so it forms a natural montonicty of the answers where incresing weight capcity forms a montocity
        # of wther or not it si even possible to do in the given days to load all wieghts by the belt
        n = len(weights)
        r = sum(weights)
        l = max(weights)

        def possible(wlimit):
            # we use a greedy apporach
            # we load as much ina. day as possible
            # as soon as we exceed capcity we call it a day
            time = days
            tot = 0
            for weight in weights:
                if tot + weight > wlimit:
                    tot = weight
                    time -= 1
                else:
                    tot += weight
            return time > 0


        # return first true answer space possible
        while l < r:
            m = (l+r) // 2
            if possible(m): r = m
            else: l = m + 1
        
        return l