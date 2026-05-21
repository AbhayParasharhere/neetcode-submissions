class Solution:
    def decodeString(self, s: str) -> str:
        n = len(s)
        till = 0
        stack = deque()
        res = ""

        while till <  n:
            numStr = ""
            while s[till].isnumeric():
                numStr += s[till]
                till += 1
            if numStr != "":
                stack.append(numStr)
            stack.append(s[till])
            if s[till] == "]":
                stack.pop()
                # sign to process stack to find res
                parts = []
                while stack and stack[-1] != "[":
                    parts.append(stack.pop())
                if stack:
                    stack.pop() # removes the opening bracket
                    times = 1
                    if stack:
                        times = stack.pop()
                    repeat = ''.join(reversed(parts))
                    stack.append( repeat * int(times))
            till += 1
        return ''.join(stack)

