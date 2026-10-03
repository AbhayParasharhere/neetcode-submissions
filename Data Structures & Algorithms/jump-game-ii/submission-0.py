class Solution:
    def jump(self, nums: List[int]) -> int:
        # # same idea as jump game where the logic of going forward not backward

        # # anytime we reach the destination index our our amx hop is destination we also keep track of hwo many hops it took us, and keep track of min hops taken as well

        # curHops = 0
        # canReach = 0
        # n = len(nums)

        # target = n - 1

        # for i in range(n):
        #     curCanReach = i + nums[i]
        #     if curCanReach == target:
        #         return curHops  + 1
        #     if i == canReach:
        #         # we are standing at the max range
        #         #  so clearly we need more hops to reach the target
        #         curHops += 1
        # return 

        # look at this as a graph porblem we have teh adj list given by the jump radius 
        # so we need to do a bfs and if we reach the end index we return minm cost

        n = len(nums)
        if n == 1: return 0
        q = deque()
        visited = [False] * n
        q.append((0,nums[0]))
        visited[0] = True

        level = 0
        while q:
            level += 1
            for _ in range(len(q)):
                popped_u,jump = q.popleft()
                if popped_u + jump >= n-1:
                    return level
                # all the vertices in my jump radius are my neighbouts
                for v in range(popped_u + 1,min(popped_u + jump+1,n)):
                    if not visited[v]:
                        visited[v] = True
                        q.append((v,nums[v]))

            
