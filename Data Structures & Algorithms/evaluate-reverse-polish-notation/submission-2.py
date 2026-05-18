class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = {
            "+","-","*","/"
        }

        stack = deque()

        for ch in tokens:
            if ch not in ops:
                stack.append(ch)
            else:
                op = ch
                # perform op on last two on tsack and push res back to stack
                op1 = int(stack.pop())
                op2 = int(stack.pop())
                if op == "+":
                    stack.append(op1 + op2)
                elif op == "-":
                    stack.append(op2 - op1)
                elif op == "*":
                    stack.append(op1 * op2)
                elif op == "/":
                    stack.append(op2/op1)
                    
        return int(stack.pop())