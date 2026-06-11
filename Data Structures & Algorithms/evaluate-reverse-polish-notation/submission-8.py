class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = {"+","-","*","/"}
        stack = []

        for tok in tokens:
            # print(stack)
            if tok in ops:
                op2 = stack.pop()
                op1 = stack.pop()
                if tok == "+": res = op1 + op2
                elif tok == "-": res = op1 - op2
                elif tok == "*": res= op1 * op2
                else: res = int(op1/op2)
                stack.append(res)
            else:
                print(tok)
                stack.append(int(tok))

        return stack.pop() if stack else -1
