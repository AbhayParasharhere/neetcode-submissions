import heapq
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        # create zip pair
        # create min heap by capital
        hp_cap = list(zip(capital,profits))
        cur_cap = w
        heapq.heapify(hp_cap)
        hp_can_do = []
        
        # choose all k prjects or as many proj as choosing more doest hurt as profit > 0
        for i in range(min(k,len(profits))):
            # print(hp_cap,hp_can_do,hp_cap[0][0],cur_cap)
            # shave all whose capital we can afford into a max heap
            while hp_cap and hp_cap[0][0] <= cur_cap:
                _,popped_pro = heapq.heappop(hp_cap)
                # ordered by profit
                heapq.heappush_max(hp_can_do,popped_pro)
                # print('pushed',popped_pro,hp_can_do)
            # choose the top one and do it
            # print(i,hp_can_do)
            if not hp_can_do:
                # the speacial case when nothing is permitted so hp can do is always empty
                return cur_cap
            to_add = heapq.heappop_max(hp_can_do)
            cur_cap += to_add
        return cur_cap


