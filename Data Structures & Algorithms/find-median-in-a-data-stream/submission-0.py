class MedianFinder:

    def __init__(self):
        # lheap is a max heap, rheap is a min heap of the right half
        self.lheap = []
        self.rheap = []


    def addNum(self, num: int) -> None:
        # append to right heap first
        heapq.heappush(self.rheap,num)
        if self.lheap and self.rheap[0] < self.lheap[0]:
            # pop push to right heap
            popped = heapq.heappop(self.rheap)
            heapq.heappush_max(self.lheap,popped)
        
        # balance them out
        # lheap overflow
        if self.lheap and len(self.lheap) > len(self.rheap):
            popped = heapq.heappop_max(self.lheap)
            heapq.heappush(self.rheap,popped)
            return
        # rheap overflow
        if len(self.rheap) > 1  and len(self.rheap) > len(self.lheap) + 1:
            popped = heapq.heappop(self.rheap)
            heapq.heappush_max(self.lheap,popped)
            return


    def findMedian(self) -> float:
        # print(self.lheap,self.rheap)
        if (len(self.lheap) + len(self.rheap)) % 2 != 0:
            return float(self.rheap[0])
        else:
            return (float(self.rheap[0]) + float(self.lheap[0])) / 2

        
        