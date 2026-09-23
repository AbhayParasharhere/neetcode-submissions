import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # push standard nums and manintain a min heap
        self.hp = [num for num in nums]
        self.k = k
        heapq.heapify(self.hp)
        

    def add(self, val: int) -> int:

        heapq.heappush(self.hp,val)
        # force a size of k to the heap so that heap stores the kth smallest at the top
        # we discard all the use less elements which are less that kth largest element
        while len(self.hp) > self.k:
            heapq.heappop(self.hp)
        # now the top of min heap is the kth largest 
        return self.hp[0]