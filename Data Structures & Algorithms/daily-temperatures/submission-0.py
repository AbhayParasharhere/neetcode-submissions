class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # heard using montonic stack which keeps stack only in strictly increasing order or decreasing
        n = len(temperatures)
        stack = deque()
        res = [0 for _ in range(n)]
        for i, temp in enumerate(temperatures):
            while stack and temp > temperatures[stack[-1]]:
                to_put = stack.pop()
                res[to_put] = i - to_put
            stack.append(i)
        return res

