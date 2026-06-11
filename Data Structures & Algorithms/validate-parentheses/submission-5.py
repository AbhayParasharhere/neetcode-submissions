class Solution:
    def isValid(self, s: str) -> bool:
        close = {"}":"{","]":"[",")":"("}
        stack = []

        for br in s:
            if br in close:
                opn = close[br]
                if not stack or stack[-1] != opn:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(br)
        return len(stack) == 0
                