class Solution:
    def simplifyPath(self, path: str) -> str:
        paths = path.split('/')
        special = {'..','.',''}
        stack = deque()

        for p in paths:
            if p in special:
                if p == "..": 
                    if stack: stack.pop()
                elif p == "." or p == "": continue

            else:
                stack.append(p)
        return "/" + '/'.join(list(stack))
