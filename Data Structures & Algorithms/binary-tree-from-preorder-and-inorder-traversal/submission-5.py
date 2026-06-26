# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # we use divide and conquer wher inorder and preorder are divided ine ach child
        # for them to get their own root and their own left andright child

        # first val in preorder is the root
        # anything until we find that in order to the left are the lt subtree
        # anything to its right are the rt subtree
        # every node retuns its addres back to its parent
        # parent attaches their children

        # for o1 lookup of partition
        in_map = {val:i for i,val in enumerate(inorder)}

        def build(pre_st,pre_end,in_st,in_end):
            if in_st > in_end:
                # off bound eventually for null pointers
                return None

            root_val = preorder[pre_st]
            partition = in_map[root_val]
            left_size = partition - in_st

            l_pre_st = pre_st + 1
            l_pre_end = pre_st + left_size
            r_pre_st = l_pre_end + 1
            r_pre_end = pre_end

            l_in_st = in_st
            l_in_end = in_st + left_size - 1
            r_in_st = l_in_end + 2
            r_in_end = in_end
            node = TreeNode(root_val)

            node.left = build(l_pre_st,l_pre_end,l_in_st,l_in_end)
            node.right = build(r_pre_st,r_pre_end,r_in_st,r_in_end)

            return node
        return build(0,len(preorder)-1,0,len(inorder)-1)
