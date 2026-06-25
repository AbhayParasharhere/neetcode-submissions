# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        
        Dq = deque()
        Dq.append(root)
        res = []
        # template level order traversal
        # keep popping left and that is a level, 
        # whithin that proess them and then add left and right children in q to the end
        while Dq:
            level_len = len(Dq)
            level_child = []
            for r in range(level_len):
                node = Dq.popleft()
                level_child.append(node.val)
                if node.left: Dq.append(node.left)
                if node.right: Dq.append(node.right)
            res.append(level_child)
        return res

