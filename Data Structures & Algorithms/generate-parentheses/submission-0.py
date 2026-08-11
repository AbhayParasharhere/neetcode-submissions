class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(op_left,cl_left,path,cl_need):
            if len(path) == 2*n and op_left == 0 and cl_left == 0:
                res.append("".join(path))
                return
            if len(path) > 2*n:
                return
            
            # 2 choices at every level - put open brackets or put close brakcets
            # case put open brackets
            # every open bracket geenrets its own closing need
            if op_left > 0:
                path.append("(")
                cl_need += 1
                backtrack(op_left - 1,cl_left,path,cl_need)
                path.pop()
                cl_need -= 1
            # case where we don't put close brackets if last is not open
            if cl_left > 0 and cl_need > 0:
                path.append(")")
                cl_need -= 1
                backtrack(op_left,cl_left -1,path,cl_need)
                path.pop()
                cl_need += 1
        backtrack(n-1,n,["("],1)
        return res
            