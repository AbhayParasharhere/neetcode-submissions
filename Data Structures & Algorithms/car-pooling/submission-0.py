class Solution:
    def carPooling(self, trips: list[list[int]], capacity: int) -> bool:
        h1 = [(st,cap,end) for cap, st,end in trips]
        heapq.heapify(h1)
        h2 = []
        cur_cap = 0

        while h1 or h2:
            # pick up everyone who boards before the next drop-off
            while h1 and (not h2 or h1[0][0] < h2[0][0]):
                p_st,p_cap,p_end = heapq.heappop(h1)
                cur_cap += p_cap
                heapq.heappush(h2,(p_end,p_st,p_cap))
                if cur_cap > capacity:
                    return False
            # drop off the earliest passenger
            if h2:
                p_end,p_st,p_cap = heapq.heappop(h2)
                cur_cap -= p_cap
        return True