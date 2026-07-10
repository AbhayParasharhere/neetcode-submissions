# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        # we can do a dfs preorder traversal, but rmeber that null nodes are stored as null
        # in the res array
        # fianlly in deserialize we do the proerder itreation again on the input array
        # recognizing null as the empty child
        res = []
        def dfs(node):
            nonlocal res
            if not node: return res.append("Null")
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return ",".join(res)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data: return None
        vals = data.split(',')
        self.i = 0
 
        def dfs():
            if vals[self.i] == "Null":
                self.i += 1
                return None
            node = TreeNode(int(vals[self.i]))
            self.i += 1
            node.left = dfs()
            node.right = dfs()
            return node
       
        return dfs()
        
