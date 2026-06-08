class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        stack = deque()
        res = [0 for _ in range(n)]

        for i in range(n):
            tmp = temperatures[i]
            while stack and temperatures[stack[-1]] < tmp:
                # we are at a warmer day than any of our stack 
                fill_at = stack.pop()
                res[fill_at] = i - fill_at
            stack.append(i)
        return res