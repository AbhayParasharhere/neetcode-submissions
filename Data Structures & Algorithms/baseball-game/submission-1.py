class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = deque()
        ops = {"+","C","D"}

        for op in operations:
            if op in ops:
                if op == "+":
                    if len(stack) >= 2:
                        tot = int(stack[-1]) + int(stack[-2])
                        stack.append(int(tot))
                if op == "D":
                    if stack: stack.append(int(stack[-1] * 2))
                if op == "C": 
                    if stack: stack.pop()
            else:
                stack.append(int(op))
        return sum(stack)