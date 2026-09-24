import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # geta. min heap of size k so forcing size k means top will contain kt largest element

        hp = [num for num in nums]
        heapq.heapify(hp)

        # pop until heap is of size k
        while len(hp) != k:
            # throw uselss elements which are less than kth largets
            # print(hp)
            heapq.heappop(hp)
        return hp[0]