from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        # put the char in stack we are always doing the check against teh prev char
        # so if not equal then false
        # if tehya re opening bracket keep pushing them on stack
        # if we theya re closing bracket - pop the last elemnt and if same continue else push
        key = {"(": ")", "{": "}", "[": "]"}
        stack = deque()

        for bracket in s:
            if bracket in key:
                # its an opening bracket
                stack.append(bracket)
            else:
                # try the top of stack
                if len(stack) < 1:
                    return False
                if key[stack.pop()] != bracket:
                    return False
            
        if len(stack) > 0:
            return False

        return True
