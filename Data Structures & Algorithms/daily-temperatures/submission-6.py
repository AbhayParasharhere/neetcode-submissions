class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # we are intersted in temp greater then ourself ahead of us
        # so we are interested in a montonic decreasing as grater is the limit
        # when we encounter the greater it pops all less than it and assisng the correct disstacne fromt hem as the answer to them
        
        n = len(temperatures)
        res = [0 for _ in range(n)]
        stack = []

        for i in range(n):
            temp = temperatures[i]
            while stack and temperatures[stack[-1]] < temp:
                popped = stack.pop()
                res[popped] = i - popped
            # we store indexes to cal distance in future easily
            stack.append(i)
        
        return res
