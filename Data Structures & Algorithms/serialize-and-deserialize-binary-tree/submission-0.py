# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root: return ""
        dq = deque()
        dq.append(root)
        res = []

        while dq:
            level = len(dq)
            for _ in range(level):
                node = dq.popleft()
                if node: 
                    # the "," is necessary for multi digit values
                    res.append(str(node.val))
                    dq.append(node.left)
                    dq.append(node.right)
                else:
                    # we are at None node so nothing to push
                    # * represents null
                    res.append("*")
        return ",".join(res)      
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data: return None
        tokens = data.split(",")
        root = TreeNode(int(tokens[0]))
        dq = deque([root])
        i = 1
        while dq and i < len(tokens):
            node = dq.popleft()
            if tokens[i] != "*":
                node.left = TreeNode(int(tokens[i]))
                dq.append(node.left)
            i += 1
            if i < len(tokens) and tokens[i] != "*":
                node.right = TreeNode(int(tokens[i]))
                dq.append(node.right)
            i += 1
        return root