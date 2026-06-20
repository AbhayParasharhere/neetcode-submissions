# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # we can have a function that checks if 1 tree is equal to another
        # then we run that function for every node in out tree
        # if any of node is the same as q then yea that q is considered a subtree we return true

        def same(p,q):
            if not p and not q: return True
            if not p or not q: return False

            # Again pre order to check for any mismatch - limiting factor is True false eveywhere else
            if p.val == q.val:
                lsame = same(p.left,q.left)
                rsame = same(p.right,q.right)
                return lsame and rsame
            else:
                return False
        def isSub(p,q):
            if not p: return False
            # null is subtree of every tree
            if not q: return True

            isSame = same(p,q)
            if isSame: return True
            # recurse on left and right nodes of p
            # pre order traversal top down
            return isSub(p.left,q) or isSub(p.right,q)
        return isSub(root,subRoot)
