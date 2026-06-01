class Solution:
    def isValid(self, s: str) -> bool:
        close = {")": "(", "]": "[", "}": "{"}
        stack = deque()

        for br in s:
            if br in close:
                # now we must process to ensure validity
                if stack and stack[-1] != close[br]:
                    # invalid bracket where its correct opens should be
                    return False
                else:
                    if stack: stack.pop()
                    else: return False
            else:
                stack.append(br)
        return True if len(stack) == 0 else False
