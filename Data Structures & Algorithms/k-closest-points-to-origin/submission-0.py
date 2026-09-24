import math, heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        for i,(x,y) in enumerate(points):
            dist = math.sqrt(((x-0)*(x-0)) + ((y-0)*(y-0)))
            points[i] = (dist,x,y)
        heapq.heapify(points)
        res = []
        for i in range(k):
            to_append = heapq.heappop(points)
            res.append([to_append[1],to_append[2]])
        return res