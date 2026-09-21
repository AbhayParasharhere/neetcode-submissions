import heapq
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # # djikstra but we maintain teh steps it took so faror k
        # # and we dont push those with higher k in the heap at all
        
        hp = []
        res = [(float('inf'),float('inf'))] * n

        adj = {u:[] for u in range(n)}

        for u,v,cost in flights:
            adj[u].append((cost,v))

        # src to src is 0
        res[src] = (0,0)
        # we store steps_took,cost,v
        hp.append((0,0,src))

        while hp:
            steps_took,cost_from_source, u = heapq.heappop(hp)
            # all my nieghborus from now on will have oen more step as it includes me
            # in the path
            # if res[u] < cost_from_source : continue
            # if u == dst:
            #     return cost_from_source if steps_took <= k else -1
            if steps_took > k : continue
            steps_took += 1

            for cost,v in adj[u]:
                total = cost + cost_from_source
                if (total,steps_took) < res[v]:
                    res[v] = (total,steps_took)
                    heapq.heappush(hp,(steps_took,total,v))
        return res[dst][0] if res[dst][0] != float('inf') else -1

        # lets try bellman ford but maintain max hops count for each node from src


        # res = {}
        # hops = {}

        # res[src] = [0]
        # hops[src] = [-1]
        # # relax edges n -1 times
        # for _ in range(n-1):
        #     for u,v,w in flights:
        #         # we want to store all routes through all possible hops and selcted
        #         # the chepest but still within our hop limit
        #         if u not in hops or u not in res:
        #             # as key doenst exist we havent stored any path teher yet
        #             continue
        #         # find teh cheapest hop and cost pair
        #         for u in range(len(hops[src])):
                     
        #         new_hops_to_v = hops[u] + 1
        #         if new_hops_to_v > k:
        #             # we dont want to pollute the future count with out of bounds hops
        #             # so neevr update anything from exceeded hops paths
        #             continue
        #         total_to_v = res[u] + w
        #         if total_to_v <= res[v]:
        #             res[v] = total_to_v
        #             hops[v] = new_hops_to_v
        # print(res,hops,dst,res[dst])
        # return res[dst] if res[dst] != float('inf') else -1

