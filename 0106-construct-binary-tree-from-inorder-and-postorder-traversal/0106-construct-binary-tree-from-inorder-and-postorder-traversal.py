# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        n = len(postorder) - 1
        mpp = {value: index for index, value in enumerate(inorder)}

        def helper(postorder, ps, pe, inorder, ins, ie, mpp):
            if ps > pe or ins > ie:
                return None
            root = TreeNode(postorder[pe])
            inroot = mpp[postorder[pe]] 
            lhs = inroot - ins  

            root.left = helper(postorder, ps, ps + lhs - 1, inorder, ins, inroot - 1, mpp)
            root.right = helper(postorder, ps + lhs, pe - 1, inorder, inroot + 1, ie, mpp)
            return root

        return helper(postorder, 0, n, inorder, 0, len(inorder) - 1, mpp)