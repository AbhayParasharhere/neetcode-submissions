# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []
        def dfs(node):
            if not node: 
                res.append("None")
                return res
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return ",".join(res)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        arr = data.split(",")
        at = 0
        # every node returns its address to its parent so parent can form a tree
        def dfs():
            nonlocal at
            if at == len(data) or arr[at] == "None":
                return None
            node = TreeNode(arr[at])
            at += 1
            node.left = dfs()
            at += 1
            node.right = dfs()
            return node
        
        # print(root)
        return dfs()
