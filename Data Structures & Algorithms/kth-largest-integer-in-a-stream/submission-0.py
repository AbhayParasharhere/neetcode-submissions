import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # if we push the negatuve of values then min heap will act as a max heap
        self.hp = []
        self.k = k
        for num in nums:
            heapq.heappush(self.hp,(-1*num))

    def add(self, val: int) -> int:
        heapq.heappush(self.hp,(-1*val))
        
        # pop k times to get the kth largest
        temp = []
        for i in range(self.k):
            temp.append(heapq.heappop(self.hp))
        res = -1 * temp[-1]
        # finally append teh leftovers
        for leftover in temp:
            heapq.heappush(self.hp,leftover)
        return res