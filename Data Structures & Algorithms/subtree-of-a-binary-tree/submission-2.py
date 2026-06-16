# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSame(p,q):
            # False is the limitingf actor here if any node is not same
            # we early return false, only true when eveyrthing is distilled to True
            # when we reach the null of both nodes from their leaf
            if not p and not q: return True
            if not p or not q: return False
            mesame = p.val == q.val
            if not mesame:
                return False
            lsame = isSame(p.left,q.left)
            rsame = isSame(p.right,q.right)
            return lsame and rsame

        def isSub(p,q):
            if not p: return False
            if not q: return True
            meSame = isSame(p,q)
            lcontains = isSub(p.left,q)
            rcontains = isSub(p.right,q)
            return lcontains or rcontains or meSame

        return isSub(root,subRoot)