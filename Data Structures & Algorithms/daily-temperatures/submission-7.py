class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #  use a montonic decreaisng stack as interested in next greater
        # when greater comes from teh start it pops stuff from the stack less than it
        # and assigns the distacne to them as their res
        n = len(temperatures)
        res = [0 for _ in range(n)]
        stack = []

        for i in range(n):
            cur_temp = temperatures[i]

            while stack and temperatures[stack[-1]] < cur_temp:
                less_temp_index = stack.pop()
                res[less_temp_index] = i - less_temp_index
            stack.append(i)

        return res