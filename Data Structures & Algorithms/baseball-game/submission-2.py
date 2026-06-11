class Solution:
    def calPoints(self, operations: List[str]) -> int:
        exc = ["+","C","D"]
        stack = deque()

        for op in operations:
            if op in exc:
                if op == "+":
                    op2 = int(stack[-1])
                    op1 = int(stack[-2])
                    stack.append(op1+op2)
                elif op == "C":
                    stack.pop()
                elif op == "D":
                    stack.append(int(stack[-1]) * 2)
            else:
                stack.append(int(op))
        return sum(list(stack))