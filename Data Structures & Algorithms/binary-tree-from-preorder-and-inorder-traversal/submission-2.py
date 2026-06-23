# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # we are doing bottom up apparach and using 4 indexes pre start, pre end, ins atrt and ined 
        # this is becasuse first val in pre order is always the root
        # in roder until we find that val everything to its left is the left subtree
        # evreythingt o its right is the right subtree
        # when we find the root value or teh partion
        # then the elft subtree size is partition - instart absolute val as its positive
        # base case is when inend > instart or simple l > r 2 poinetr like abse case
        # we create a hashmap of inorder for o1 lookups of val to index
        in_map = {val:i for i, val in enumerate(inorder)}

        def build(pre_start,pre_end,in_start,in_end):
            # base case when indexes cross so we reach teh null and return none
            # the return value of every node is its address back to its parent to attach cleanly
            if in_start > in_end: return None

            root_val = preorder[pre_start]
            partition = in_map[root_val]
            left_size = partition - in_start
            node = TreeNode(root_val)

            left_pre_start = pre_start + 1
            left_pre_end = pre_start + left_size

            right_pre_start = left_pre_end + 1# or pre_start + left_size + 1
            right_pre_end = pre_end

            left_in_start = in_start
            left_in_end = in_start + left_size - 1

            right_in_start = in_start + left_size + 1
            right_in_end = in_end

            # our left subtree is given its approiate arrays bounds
            node.left = build(left_pre_start,left_pre_end,left_in_start,left_in_end)
            node.right = build(right_pre_start,right_pre_end,right_in_start,right_in_end)
            # evernutally building up we return the root
            return node
        return build(0,len(preorder) - 1,0,len(inorder) - 1)