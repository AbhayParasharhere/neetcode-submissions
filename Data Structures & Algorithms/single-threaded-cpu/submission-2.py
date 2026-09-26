import heapq
class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        # push original indexes 
        # we will use 2 heaps teh first to know which task to start with
        # other h2 to know which among the start we can pick the bets one

        for i, task in enumerate(tasks):
            task.append(i)
        
        time = 1
        h1 = []
        h2 = []
        res = []
        for task in tasks:
            # sort just by start time,process time, org index
            h1.append(task)
        heapq.heapify(h1)
        
        while h1:
            # process all who are less than current time into h2
            # or just the top when cur time < h1 top
            top_time = h1[0][0]
            if not h2 and time < top_time:
                popped = heapq.heappop(h1)
                # h2 just orders from porces tiem and orginal i
                heapq.heappush(h2,(popped[1],popped[2]))
                time = top_time
            else:
                while h1 and h1[0][0] <= time:
                    popped = heapq.heappop(h1)
                    # print('popped',popped)
                    heapq.heappush(h2,(popped[1],popped[2]))
            # now we process tasks from h2
            # print(h2)
            process = heapq.heappop(h2)
            res.append(process[1])
            # print(process)
            time += process[0]

        # now tehr emight still be elements left from h2 in the end 
        # means all task are ready
        # teh orider is simply teh pop order in h2 now
        while h2:
            process = heapq.heappop(h2)
            res.append(process[1])
            time += process[0]
        return res

