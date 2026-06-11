class Solution:
    def simplifyPath(self, path: str) -> str:
        exc = {"..","."}

        paths = [p for p in path.split("/") if p!= ""]
        stack = []

        for p in paths:
            if p in exc:
                if p == ".." and stack: 
                    stack.pop()
            else: stack.append(p)
        return "/" + "/".join(list(stack))