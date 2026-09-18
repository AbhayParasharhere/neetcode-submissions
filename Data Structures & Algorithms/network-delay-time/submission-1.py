import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # use djikstra and teh final result is teh maxim time it took

        # create graph
        adj = {u: [] for u in range(n+1)}

        res = [float('inf')] * (n+1)
        visited = [False] * (n+1)

        # create graph
        for u,v,w in times:
            adj[u].append((w,v))

        # append the source
        # time from source to source is 0
        res[k] = 0
        hp = []
        hp.append((0,k))
        visited[k] = True
        max_time = float('-inf')
        while hp:
            time_from_source,u = heapq.heappop(hp)
            # decided so stop guessingf or this node
            visited[u] = True
            if res[u] < time_from_source: continue

            for t,v in adj[u]:
                total_time = t + time_from_source
                if total_time < res[v]:
                    res[v] = total_time
                    heapq.heappush(hp,(total_time,v))
        for time in res[1:]:
            if time == float('inf'):
                return -1
            else:
                max_time = max(max_time,time)
            
        return max_time


