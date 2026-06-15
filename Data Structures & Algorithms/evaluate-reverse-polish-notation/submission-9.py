class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = {"+","-","*","/"}
        stack = []

        for tok in tokens:
            if tok in ops:
                op2 = stack.pop()
                op1 = stack.pop()
                if tok == "+": stack.append(op1+op2)
                elif tok == "-": stack.append(op1-op2)
                elif tok == "*": stack.append(op1*op2)
                else: stack.append(int(op1/op2))
            else:
                stack.append(int(tok))
        return stack.pop() if stack else -1 
