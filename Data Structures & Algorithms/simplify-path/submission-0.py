class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = deque()
        all_actions = [item for item in path.split("/") if item]
        for action in all_actions:
            if action == "..":
                if stack:
                    stack.pop()
            elif action == ".":
                continue
            else:
                stack.append(action)
        
        return f"/{'/'.join(stack)}"