import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        hp = [-1 * s for s in stones]
        # get max heap
        heapq.heapify(hp)
        while len(hp) >= 2:
            first = -1 * heapq.heappop(hp)
            second = -1 * heapq.heappop(hp)

            left = first - second
            if left != 0:
                heapq.heappush(hp,-1 * left)
        return -1 * hp[0] if hp else 0