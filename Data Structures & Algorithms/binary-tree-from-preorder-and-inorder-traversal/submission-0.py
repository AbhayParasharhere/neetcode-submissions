# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # preorder 1st value is teh root
        # in inorder we find the pre oder value everything until we find it is teh left subtree
        # so we do a recursive call with this half as the inorder array
        # the root val again is the first val from the left whcih is unmarked as the root val in this
        # if the inorder array passed is empty then both left and right child are none
        # every iteration returns teh node val in the end
        def build(preorder,inorder):
            if not inorder: return None
            # base case
            if len(inorder) == 1: 
                return TreeNode(inorder[0],None,None)

            # we also trim down preorder by 1 in each passing
            rootVal = preorder[0]
            idxRoot = inorder.index(rootVal)
            leftInorder = inorder[0:idxRoot]
            rightInorder = inorder[idxRoot+1:len(inorder)]
            leftPreorder = preorder[1:1+idxRoot]
            rightPreorder = preorder[1+idxRoot:]

            # create node and recurse left and right for the left and right node
            node = TreeNode(rootVal)
            node.left = build(leftPreorder,leftInorder)
            node.right = build(rightPreorder,rightInorder)

            # return it for our parent
            return node
        
        return build(preorder,inorder)

