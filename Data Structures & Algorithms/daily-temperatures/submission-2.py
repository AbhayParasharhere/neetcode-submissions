class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # we use a montonic decreasing stack here
        # so that we are keeping track of our maximums

        stack = deque()
        n = len(temperatures)
        res = [0 for _ in range(n)]

        for i in range(n-1,-1,-1):
            temp = temperatures[i]
            while stack and temperatures[stack[-1]] <= temp:
                stack.pop()
            put = stack[-1] - i if stack else 0
            res[i] = put
            stack.append(i)
        return res
