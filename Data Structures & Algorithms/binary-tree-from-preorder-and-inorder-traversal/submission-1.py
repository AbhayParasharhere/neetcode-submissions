# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # we use the principle that firt of preorder is the root
        # until we find that in inorder everything to its elft is teh part of left subtree
        # everything to rt is part of tits right subtree
        # we can use bottom up postorder approach to create the whole recusion tree
        # by passing the apporapite idnex to where their psot order and indorer is supposed to be
        # for that specific subtree we are recusing

        # we can use a hmap for node value to array indexing in inorer array
        # maps the node val to index
        inmap = {val:i for i, val in enumerate(inorder)}

        # in recursion every node will return its address back to its aprent
        # if need be child will construct then return
        
        def build(pstart,pend,instart,inend):
            if pstart > pend:
                return None
            node = TreeNode(preorder[pstart])
            partition = inmap[preorder[pstart]]
            leftSize = partition - instart
            # this is the index conversion mapping to get the valid left and rigth partion
            node.left = build(pstart+1,pstart + leftSize,instart,partition-1)
            node.right = build(pstart + leftSize + 1,pend,partition+1,inend)
            return node
        return build(0,len(preorder) - 1,0,len(inorder) - 1)
            