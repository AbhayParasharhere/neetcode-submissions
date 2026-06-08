class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # using decreasing stack from teh end in rverse
        # as the our intrest or limit becomes the prev greater temp
        # every smaller one that comes inherits this and puts themselves in this order

        stack = deque()
        n = len(temperatures)
        res = [0 for _ in range(n)]
        for i in range(n-1,-1,-1):
            temp = temperatures[i]
            # print(i,stack[-1] if stack else 'none',stack)
            while stack and temperatures[stack[-1]] <= temp:
                stack.pop()
            # Now stack top contains the greatest temp to the right for the temp
            res[i] = stack[-1] - i if stack else 0
            stack.append(i)
        return res
