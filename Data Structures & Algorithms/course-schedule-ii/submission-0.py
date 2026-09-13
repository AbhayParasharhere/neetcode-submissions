from collections import deque
from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        V = numCourses
        mp = {u: [] for u in range(V)}
        in_degree = [0] * V
        
        # Build adjacency list and calculate in-degrees
        for v, u in prerequisites:
            mp[u].append(v)
            in_degree[v] += 1
            
        # Queue all nodes with no dependencies (in-degree 0)
        queue = deque([u for u in range(V) if in_degree[u] == 0])
        topo = []
        
        while queue:
            u = queue.popleft()
            topo.append(u)
            
            for v in mp[u]:
                in_degree[v] -= 1
                if in_degree[v] == 0:
                    queue.append(v)
                    
        # If topo doesn't include all courses, a cycle exists
        return topo if len(topo) == V else []
