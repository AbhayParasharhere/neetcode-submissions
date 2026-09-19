import heapq
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # can use prims to fidn teh mst which is what we need here
        mst = 0

        hp = []
        visited = set()

        hp.append((0,(points[0][0],points[0][1])))

        while hp:
            cost,(ui,uj) = heapq.heappop(hp)

            if (ui,uj) in visited: continue
            visited.add((ui,uj))
            mst += cost
            # like djikstra its decided to add this min edge to mst


            # complete graph so connected toe verything
            for vi,vj in points:
                if (vi,vj) not in visited:
                    edge_cost_here = abs(ui-vi) + abs(uj-vj)
                    # push every guess no need to decide only the smalelst like we do in djisktra
                    heapq.heappush(hp,(edge_cost_here,(vi,vj)))
        return mst