from collections import deque
class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = deque()
        for op in operations:
            if op == "C":
                if len(stack) > 0:
                    stack.pop()
            elif op == "+":
                if len(stack) >= 2:
                    toPut = int(stack[-1]) + int(stack[-2])
                    stack.append(toPut)
            elif op == "D":
                if len(stack) >=1:
                    stack.append(2 * stack[-1])
            else:
                stack.append(int(op))
        
        return sum(int(item) for item in stack)
        