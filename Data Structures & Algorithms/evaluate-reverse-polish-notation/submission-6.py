class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = {"+","-","*","/"}
        stack = deque()

        for tok in tokens:
            print(stack)
            if tok in ops:
                if len(stack) >=2:
                    op1 = int(stack.pop())
                    op2 = int(stack.pop())
                else:
                    # invalid case
                    return
                if tok == "+":
                    stack.append(op2+op1)
                elif tok == "-":
                    stack.append(op2-op1)
                elif tok == "*":
                    stack.append(op2*op1)
                else:
                    stack.append(int(op2/op1))
            else:
                stack.append(int(tok))
        if stack: return stack.pop()